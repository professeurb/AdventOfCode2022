#require "Brulib"

open Brulib

(* let file = "test05.txt" *)
let file = "input05.txt"

let read_crates gen =
  let lines = ref [] in
  let rec get_crates () =
    let line = gen () |> Option.value in
    if line.[1] = '1' then (
      let nb = (1 + String.length line) / 4 in
      let crates = Array.make nb [] in
      List.iter
        (fun line ->
          for i = 0 to nb - 1 do
            let c = line.[(4 * i) + 1] in
            if c <> ' ' then crates.(i) <- c :: crates.(i)
          done)
        !lines;
      crates)
    else (
      lines := line :: !lines;
      get_crates ())
  in
  get_crates ()

let _ =
  let strm = Gen.of_file file in
  let crates1 = read_crates strm in
  let crates2 = Array.copy crates1 in
  assert (strm () = Some "");
  Gen.iter
    (fun line ->
      Scanf.sscanf line "move %d from %d to %d"
        (fun cnt src dst ->
          let ll = ref [] in
          for i = 1 to cnt do
            (* Part One *)
            (match crates1.(src - 1) with
            | a :: l ->
                crates1.(src - 1) <- l;
                crates1.(dst - 1) <- a :: crates1.(dst - 1)
            | [] -> failwith "Part One");
            match crates2.(src - 1) with
            | a :: l ->
                crates2.(src - 1) <- l;
                ll := a :: !ll
            | [] -> failwith "Part Two"
          done;
          crates2.(dst - 1) <-
            List.rev_append !ll crates2.(dst - 1)))
    strm;
  print_string "Part One: ";
  Array.iter (fun l -> print_char (List.hd l)) crates1;
  print_newline ();
  print_string "Part Two: ";
  Array.iter (fun l -> print_char (List.hd l)) crates2;
  print_newline ()
