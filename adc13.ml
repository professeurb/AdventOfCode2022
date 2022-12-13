#require "brulib"

open Brulib

(* let file = "test13.txt" *)
let file = "input13.txt"

type token = LB | RB | I of int

let tokenize s =
  Gen.of_fun (fun yield ->
      let n = String.length s in
      let rec read_any p =
        if p < n then
          match s.[p] with
          | '[' ->
              yield LB;
              read_any (p + 1)
          | ']' ->
              yield RB;
              read_any (p + 1)
          | ',' ->
              (* yield C; *)
              read_any (p + 1)
          | '0' .. '9' ->
              read_int (int_of_char s.[p] - 48) (p + 1)
          | _ -> failwith ""
      and read_int i p =
        match s.[p] with
        | '0' .. '9' ->
            read_int
              ((10 * i) + int_of_char s.[p] - 48)
              (p + 1)
        | _ ->
            yield (I i);
            read_any p
      in
      read_any 0)

type packet = PI of int | PL of packet list

let packet s =
  let t = tokenize s in
  let rec read_token () =
    match t () with
    | Some (I i) -> PI i
    | Some LB -> PL (read_list ())
    | _ -> failwith "Nothing to read"
  and read_list () =
    match t () with
    | Some (I i) -> PI i :: read_list ()
    | Some RB -> []
    | Some LB ->
        let stuff = read_list () in
        PL stuff :: read_list ()
    | _ -> failwith "Nothing to read"
  in
  read_token ()

let rec compare_packets p1 p2 =
  match (p1, p2) with
  | PL [], PL [] -> 0
  | PL [], PL _ -> -1
  | PL _, PL [] -> 1
  | PI x, PI y when x = y -> 0
  | PI x, PI y when x < y -> -1
  | PI _, PI _ -> 1
  | PI x, PL _ -> compare_packets (PL [ PI x ]) p2
  | PL _, PI y -> compare_packets p1 (PL [ PI y ])
  | PL (x :: xs), PL (y :: ys) -> (
      match compare_packets x y with
      | 0 -> compare_packets (PL xs) (PL ys)
      | c -> c)

let get_packets () =
  let data = Gen.of_file file in
  Gen.of_fun (fun yield ->
      Gen.iter
        (function "" -> () | s -> yield (packet s))
        data)

let _ =
  let packets = get_packets () in
  let good_ones =
    Gen.of_fun (fun yield ->
        let rec aux cnt =
          match packets () with
          | None -> ()
          | Some p1 ->
              let p2 = packets () |> Option.get in
              if compare_packets p1 p2 <= 0 then yield cnt;
              aux (cnt + 1)
        in
        aux 1)
  in
  Printf.printf "Part One: %d\n"
    (Gen.fold ( + ) 0 good_ones)

let _ =
  let p2 = packet "[[2]]" and p6 = packet "[[6]]" in
  let sorted_packets =
    Gen.fold (fun l p -> p :: l) [ p2; p6 ] (get_packets ())
    |> List.sort compare_packets
  in
  let score = ref 1 and pos = ref 0 in
  List.iter
    (fun x ->
      incr pos;
      if x = p2 || x = p6 then score := !pos * !score)
    sorted_packets;
  Printf.printf "Part Two: %d\n" !score
