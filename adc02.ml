#require "Brulib"

open Brulib
module Stream = Brustream

(* let file = "test02.txt" *)
let file = "input02.txt"

type coup = Pierre | Papier | Ciseaux

let bat = function
  | Pierre -> Ciseaux
  | Papier -> Pierre
  | Ciseaux -> Papier
;;

let score_coup = function
  | Pierre -> 1
  | Papier -> 2
  | Ciseaux -> 3
;;

let coup_elfe = function
  | 'A' -> Pierre
  | 'B' -> Papier
  | 'C' -> Ciseaux
  | _ -> failwith "Wrong"
;;

let coup_moi = function
  | 'X' -> Pierre
  | 'Y' -> Papier
  | 'Z' -> Ciseaux
  | _ -> failwith "Wrong"
;;

let lire_coup s = (coup_elfe s.[0], coup_moi s.[2])

let score_round (a, b) =
  score_coup b
  + if a = b then 3 else if a = bat b then 6 else 0
;;

let _ =
  let data = Stream.(of_file file |> map lire_coup) in
  let score = ref 0 in
  Stream.iter
    (fun c -> score := !score + score_round c)
    data;
  Printf.printf "Part One : %d\n" !score
;;
