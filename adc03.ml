#require "Brulib"

open Brulib
module Stream = Brustream
module CharSet = Set.Make (Char)

let file = "test03.txt"
(* let file = "input03.txt" *)

let char_score c =
  match c with
  | 'a' .. 'z' -> Char.code c - Char.code 'a' + 1
  | 'A' .. 'Z' -> Char.code c - Char.code 'A' + 27
  | _ -> failwith "Wrong item"
;;

let set_of_string s =
  String.fold_right CharSet.add s CharSet.empty
;;

let part_one s =
  let n = String.length s in
  assert (n mod 2 = 0);
  let set =
    CharSet.inter
      (String.sub s 0 (n / 2) |> set_of_string)
      (String.sub s (n / 2) (n / 2) |> set_of_string)
  in
  assert (CharSet.cardinal set = 1);
  CharSet.choose set
;;

let part_two s =
  Stream.from (fun _ ->
      try
        let s1 = set_of_string (Stream.next s)
        and s2 = set_of_string (Stream.next s)
        and s3 = set_of_string (Stream.next s) in
        let set = CharSet.(inter s1 (inter s2 s3)) in
        assert (CharSet.cardinal set = 1);
        Some (CharSet.choose set)
      with _ -> None)
;;

let _ =
  Printf.printf "Part One: %d\n"
    Stream.(
      of_file file |> map part_one |> map char_score
      |> fold ( + ) 0);
  Printf.printf "Part Two: %d\n"
    Stream.(
      of_file file |> part_two |> map char_score
      |> fold ( + ) 0)
;;
