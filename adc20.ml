(* ocamlfind ocamlopt -package Brulib -linkpkg adc20.ml -o adc20 *)

open Brulib

(* let file = "test20.txt" *)
let file = "input20.txt"
let key = 811589153

let mud a b =
  let a' = a mod b in
  if a' >= 0 then a' else a' + b

type 'a node = {
  mutable data : 'a;
  mutable prev : 'a node;
  mutable next : 'a node;
}

let new_node data =
  let rec node = { data; prev = node; next = node } in
  node

let remove node =
  node.prev.next <- node.next;
  node.next.prev <- node.prev

let insert_after left right =
  let node = left.next in
  right.next <- node;
  node.prev <- right;
  left.next <- right;
  right.prev <- left

let move_right start delta =
  if delta > 0 then (
    let next = ref start.next in
    for _ = 1 to delta - 1 do
      next := !next.next
    done;
    remove start;
    insert_after !next start)

let _ =
  let seq = Da.init () in
  Gen.(
    of_file file
    |> iter (fun v ->
           v |> int_of_string |> new_node |> Da.push seq));
  let n = Da.length seq in
  for i = 0 to n - 1 do
    (Da.get seq i).next <- Da.get seq ((i + 1) mod n);
    (Da.get seq ((i + 1) mod n)).prev <- Da.get seq i
  done;
  Da.iter
    (fun node -> move_right node (mud node.data (n - 1)))
    seq;
  let rec aux node =
    if node.data = 0 then node else aux node.next
  in
  let node = ref (aux (Da.get seq 0)) and sum = ref 0 in
  for _ = 1 to 3 do
    for _ = 1 to 1000 do
      node := !node.next
    done;
    sum := !sum + !node.data
  done;
  Printf.printf "Part One: %d\n" !sum;
  for i = 0 to n - 1 do
    let n = Da.get seq i and n' = Da.get seq ((i + 1) mod n) in
    n.next <- n';
    n'.prev <- n;
    n.data <- key * n.data
  done;
  for _ = 1 to 10 do
    Da.iter
      (fun node -> move_right node (mud node.data (n - 1)))
      seq
  done;
  let node = ref (aux (Da.get seq 0)) and sum = ref 0 in
  for _ = 1 to 3 do
    for _ = 1 to 1000 do
      node := !node.next
    done;
    sum := !sum + !node.data
  done;
  Printf.printf "Part Two: %d\n" !sum
