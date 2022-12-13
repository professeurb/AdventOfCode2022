#require "Brulib"

open Brulib

(* let file = "test07.txt" *)
let file = "input07.txt"

let rec sizes data yield =
  assert (data () = Some "$ cd /");
  let rec aux curr =
    match data () with
    | None | Some "$ cd .." -> curr
    | Some line -> (
        match line.[0] with
        | 'd' -> aux curr
        | '1' .. '9' ->
            Scanf.sscanf line "%d %s" (fun size _ ->
                aux (size + curr))
        | '$' ->
            if line.[2] = 'c' then aux (aux2 () + curr)
            else aux curr
        | _ -> failwith "Wrong line")
  and aux2 () =
    let size = aux 0 in
    yield size;
    size
  in
  ignore (aux2 ())

let _ =
  let total = ref 0 in
  Printf.printf "Part One : %d\n"
    Gen.(
      of_file file |> sizes |> of_fun
      |> tap (fun size -> total := size)
      |> filter (fun size -> size <= 100000)
      |> fold ( + ) 0);
  Printf.printf "Part Two : %d\n"
    Gen.(
      of_file file |> sizes |> of_fun
      |> filter (fun size -> size >= !total - 40000000)
      |> fold min 70000000)
