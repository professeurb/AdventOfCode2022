#require "Brulib"

open Brulib
module Stream = Brustream

(* let file = "test02.txt" *)
let file = "input02.txt"
let score_round_1 (a, b) = b + 1 + (3 * ((4 + b - a) mod 3))
let score_round_2 (a, r) = ((a + 2 + r) mod 3) + 1 + (3 * r)

let _ =
  let data =
    Stream.(
      of_file file
      |> map (fun s ->
             ( Char.code s.[0] - Char.code 'A',
               Char.code s.[2] - Char.code 'X' ))
      |> to_array)
  in
  Printf.printf "Part One : %d\n"
    (Array.fold_left
       (fun s c -> s + score_round_1 c)
       0 data);
  Printf.printf "Part Two : %d\n"
    (Array.fold_left
       (fun s c -> s + score_round_2 c)
       0 data)
;;
