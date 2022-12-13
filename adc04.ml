#require "Brulib"

open Brulib

(* let file = "test04.txt" *)
let file = "input04.txt"

let test1 a b c d =
  (* a <= b et c <= d *)
  (a <= c && d <= b) || (c <= a && b <= d)

let test2 a b c d =
  (* a <= b et c <= d *)
  (a <= c && c <= b)
  || (a <= d && d <= b)
  || (c <= a && a <= d)
  || (c <= b && b <= d)

let delta = function true -> 1 | false -> 0

let _ =
  Printf.printf "Part One: %d\n"
    Gen.(
      of_file file
      |> map (fun l -> Scanf.sscanf l "%d-%d,%d-%d" test1)
      |> map delta |> fold ( + ) 0);
  Printf.printf "Part Two: %d\n"
    Gen.(
      of_file file
      |> map (fun l -> Scanf.sscanf l "%d-%d,%d-%d" test2)
      |> map delta |> fold ( + ) 0)
