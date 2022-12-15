#require "brulib"

open Brulib

(* let file, line, maxi = ("test15.txt", 10, 20) *)
let file, line, maxi = ("input15.txt", 2000000, 4000000)
let snoc a b = b :: a

let get_data file =
  let process_data xs ys xb yb = (xs, ys, xb, yb) in
  let ss, bs =
    Gen.(
      scan_file file
        "Sensor at x=%d, y=%d: closest beacon is at x=%d, \
         y=%d"
        process_data
      |> fold
           (fun (ss, bs) (xs, ys, xb, yb) ->
             ( (xs, ys, abs (xb - xs) + abs (yb - ys)) :: ss,
               (xb, yb) :: bs ))
           ([], []))
  in
  (List.sort compare ss, List.sort_uniq compare bs)

let process_line ss y =
  let rec aux u v = function
    | (u', v') :: l when u <= v' + 1 ->
        aux (min u' u) (max v v') l
    | l -> (u, v) :: l
  in
  List.fold_left
    (fun l (xs, ys, rs) ->
      let d = rs - abs (ys - y) in
      if d >= 0 then aux (xs - d) (xs + d) l else l)
    [] ss

let rec part_two = function
  | (xl, _) :: l when xl > maxi -> part_two l
  | (xl, xr) :: l when xr >= maxi ->
      if xl <= 0 then None else Some (xl - 1)
  | _ -> None

let _ =
  let ss, bs = get_data file in
  let line_data = process_line ss line in
  Printf.printf "Part One: %d\n"
    (List.fold_left
       (fun s (a, b) -> s + b - a + 1)
       0 line_data
    - List.fold_left
        (fun s (_, y) -> if y = line then s + 1 else s)
        0 bs);
  for y = 0 to maxi do
    let line_data = process_line ss y in
    match part_two line_data with
    | Some x ->
        Printf.printf "Part Two: %d (%d, %d)\n"
          ((4000000 * x) + y)
          x y
    | _ -> ()
  done
