#require "brulib"

open Brulib

(* let file, line, maxi = ("test15.txt", 10, 20) *)

let file, line, maxi = ("input15.txt", 2000000, 4000000)
let snoc a b = b :: a

let get_data file =
  let process_data xs ys xb yb =
    (* Printf.printf *)
    (*   "Sensor at (%d, %d), closest beacon at (%d, %d)\n" xs *)
    (*   ys xb yb; *)
    (xs, ys, xb, yb)
  in
  Gen.(
    scan_file file
      "Sensor at x=%d, y=%d: closest beacon is at x=%d, \
       y=%d"
      process_data
    |> fold snoc [])

type arbre = E | N of arbre * int * int * arbre

let rec ajout_gauche a = function
  | E -> (E, a)
  | N (g, u, v, d) ->
      if a < u then ajout_gauche a g
      else if a <= v then (g, u)
      else
        let d', r = ajout_gauche a d in
        (N (g, u, v, d'), r)

let rec ajout_droite b = function
  | E -> (E, b)
  | N (g, u, v, d) ->
      if b > v then ajout_droite b d
      else if b >= u then (d, v)
      else
        let g', r = ajout_droite b g in
        (N (g', u, v, d), r)

let ajout a b t =
  assert (a <= b);
  match t with
  | E -> N (E, a, b, E)
  | _ ->
      let g, a' = ajout_gauche a t
      and d, b' = ajout_droite b t in
      N (g, a', b', d)

let rec est_dans p = function
  | E -> false
  | N (g, u, v, d) ->
      if p < u then est_dans p g else p <= v || est_dans p d

(* let rec contient a b = function *)
(*   | E -> false *)
(*   | N (g, u, v, d) -> *)
(*       if b < u then contient a b g *)
(*       else if b <= v then a >= u || contient a (u - 1) g *)
(*       else if (* b > v *) *)
(*               a > v then contient a b d *)
(*       else if a >= u then contient (v + 1) b d *)
(*       else *)
(*         (* a < u *) *)
(*         contient a (u - 1) g && contient (v + 1) b d *)

let rec prochain p = function
  | E -> p
  | N (g, u, v, d) ->
      if p < u then
        let p' = prochain p g in
        if p' = u then prochain (v + 1) d else p'
      else if p <= v then prochain (v + 1) d
      else prochain p d

let rec taille = function
  | E -> 0
  | N (g, u, v, d) -> taille g + taille d + v - u + 1

let get_line data y =
  List.fold_left
    (fun t (xs, ys, xb, yb) ->
      (* distance = abs(xb - xs) + abs (yb - ys)
         abs (x - xs) + abs (y - ys) <= distance
         abs (x - xs) <= distance - abs (y - ys)
      *)
      let d = abs (xb - xs) + abs (yb - ys) in
      let d2 = d - abs (y - ys) in
      if d2 < 0 then t else ajout (xs - d2) (xs + d2) t)
    E data

exception Line of int

let _ =
  let data = get_data file in
  let line_data = get_line data line in
  let bad_beacons =
    List.fold_left
      (fun l (_, _, xb, yb) ->
        if yb = line && est_dans xb line_data then xb :: l
        else l)
      [] data
    |> List.sort_uniq compare
    |> List.length
  in
  Printf.printf "Part One: %d\n"
    (taille line_data - bad_beacons);
  for y = 0 to maxi do
    let curr_line = get_line data y in
    let x = prochain 0 curr_line in
    if x <= maxi then
      Printf.printf "Part Two: %d (%d, %d)\n"
        ((4000000 * x) + y)
        x y
  done
(*2647448*)
