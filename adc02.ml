#require "Brulib"

open Brulib

(* let file = "test02.txt" *)
let file = "input02.txt"
let decode s = (Char.code s.[0] - Char.code 'A', Char.code s.[2] - Char.code 'X')
let score_round_1 (a, b) = b + 1 + (3 * ((4 + b - a) mod 3))
let score_round_2 (a, r) = ((a + 2 + r) mod 3) + 1 + (3 * r)

let _ =
  Printf.printf "Part One : %d\n"
    Gen.(of_file file |> map decode |> fold (fun s c -> s + score_round_1 c) 0);
  Printf.printf "Part One : %d\n"
    Gen.(of_file file |> map decode |> fold (fun s c -> s + score_round_2 c) 0)
