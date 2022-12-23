(* ocamlfind ocamlopt -package Brulib -linkpkg adc18.ml -o adc18 *)

open Brulib

(* let file = "test18.txt" *)
let file = "input18.txt"

let count_block block =
  let count = ref (3 * Hashset.length block) in
  Hashset.(
    iter
      (fun (x, y, z) ->
        if mem block (x + 1, y, z) then decr count;
        if mem block (x, y + 1, z) then decr count;
        if mem block (x, y, z + 1) then decr count)
      block);
  2 * !count

let _ =
  let drop = Hashset.init () in
  Gen.(
    scan_file file "%d,%d,%d" (fun x y z -> (x, y, z))
    |> iter (fun v -> Hashset.add drop v));
  Printf.printf "Part One: %d\n" (count_block drop);
  let xmin =
    Hashset.fold (fun m (x, _, _) -> min m x) max_int drop - 1
  and xmax =
    Hashset.fold (fun m (x, _, _) -> max m x) min_int drop + 1
  and ymin =
    Hashset.fold (fun m (_, y, _) -> min m y) max_int drop - 1
  and ymax =
    Hashset.fold (fun m (_, y, _) -> max m y) min_int drop + 1
  and zmin =
    Hashset.fold (fun m (_, _, z) -> min m z) max_int drop - 1
  and zmax =
    Hashset.fold (fun m (_, _, z) -> max m z) min_int drop + 1
  in
  let hull = Hashset.init () in
  let rec aux ((x, y, z) as p) =
    if
      xmin <= x && x <= xmax && ymin <= y && y <= ymax
      && zmin <= z && z <= zmax
      && (not (Hashset.mem drop p))
      && not (Hashset.mem hull p)
    then (
      Hashset.add hull p;
      List.iter aux
        [
          (x + 1, y, z);
          (x - 1, y, z);
          (x, y + 1, z);
          (x, y - 1, z);
          (x, y, z + 1);
          (x, y, z - 1);
        ])
  in
  aux (xmin, ymin, zmin);
  let total2 = ref (count_block hull) in
  total2 :=
    !total2 - (2 * ((xmax - xmin + 1) * (ymax - ymin + 1)));
  total2 :=
    !total2 - (2 * ((xmax - xmin + 1) * (zmax - zmin + 1)));
  total2 :=
    !total2 - (2 * ((zmax - zmin + 1) * (ymax - ymin + 1)));
  Printf.printf "Part Two: %d\n" !total2
