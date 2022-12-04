#require "Brulib"

open Brulib
module Stream = Brustream

(* let file = "test01.txt" *)
let file = "input01.txt"

let int_of_string_opt = function
  | "" -> None
  | s -> Some (int_of_string s)
;;

let _ =
  let data =
    Stream.(of_file file |> map int_of_string_opt)
    |> Da.of_stream
  in
  Da.push None data;
  let curr = ref 0
  and maxi = ref 0 in
  Da.iter
    (function
      | None ->
          maxi := max !maxi !curr;
          curr := 0
      | Some v -> curr := !curr + v)
    data;
  Printf.printf "Part One : %d\n" !maxi;
  (* Part Two *)
  let sums = Da.init ()
  and curr = ref 0 in
  Da.iter
    (function
      | None ->
          Da.heap_push (fun x y -> y - x) !curr sums;
          curr := 0
      | Some v -> curr := !curr + v)
    data;
  Printf.printf "Part Two : %d\n"
    (Da.heap_pop (fun x y -> y - x) sums
    + Da.heap_pop (fun x y -> y - x) sums
    + Da.heap_pop (fun x y -> y - x) sums)
;;
