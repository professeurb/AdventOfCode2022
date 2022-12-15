#require "brulib"

open Brulib

(* let file = "test14.txt" *)
let file = "input14.txt"

let read_line s =
  let get_coords s =
    Scanf.sscanf s "%d,%d" (fun x y -> (x, y))
  in
  let rec aux path = function
    | "->" :: c :: l -> aux (get_coords c :: path) l
    | [] -> path
    | _ -> failwith "Wrong line 2"
  in
  match String.split_on_char ' ' s with
  | [] -> failwith "Wrong line"
  | c :: l -> aux [ get_coords c ] l

let snoc a b = b :: a

let get_lines file =
  Gen.(of_file file |> map read_line |> fold snoc [])

let minmax_line =
  let rec aux (minx, maxx, miny, maxy) = function
    | (x, y) :: l ->
        aux
          (min minx x, max maxx x, min miny y, max maxy y)
          l
    | [] -> (minx, maxx, miny, maxy)
  in
  function
  | [] -> failwith "minmax_line : empty list"
  | (x, y) :: l -> aux (x, x, y, y) l

let minmax_terrain lines =
  let minx, maxx, miny, maxy =
    lines |> List.flatten |> minmax_line
  in
  (min minx 500, max maxx 500, min miny 0, max maxy 0)

let build_terrain (minx, maxx, miny, maxy) lines =
  let width = maxx - minx + 1
  and height = maxy - miny + 1 in
  let terrain = Array.make_matrix height width '.' in
  let fill xa ya xb yb =
    if xa = xb then
      for y = min ya yb to max ya yb do
        terrain.(y - miny).(xa - minx) <- '#'
      done
    else if ya = yb then
      for x = min xa xb to max xa xb do
        terrain.(ya - miny).(x - minx) <- '#'
      done
    else failwith "Wrong line"
  in
  let rec aux = function
    | (xa, ya) :: (xb, yb) :: l ->
        fill xa ya xb yb;
        aux ((xb, yb) :: l)
    | _ -> ()
  in
  List.iter aux lines;
  terrain

let drop_once terrain minx miny =
  let rec aux x y =
    if terrain.(y + 1).(x) = '.' then aux x (y + 1)
    else if terrain.(y + 1).(x - 1) = '.' then
      aux (x - 1) (y + 1)
    else if terrain.(y + 1).(x + 1) = '.' then
      aux (x + 1) (y + 1)
    else (
      terrain.(y).(x) <- 'o';
      true)
  in
  try aux (500 - minx) (0 - miny) with _ -> false

let print_terrain terrain =
  Array.iter
    (fun line ->
      Array.iter print_char line;
      print_newline ())
    terrain

let _ =
  let lines = get_lines file in
  let minx, maxx, miny, maxy = minmax_terrain lines in
  let terrain =
    build_terrain (minx, maxx, miny, maxy) lines
  in
  let rec aux cnt =
    if drop_once terrain minx miny then aux (cnt + 1)
    else cnt
  in
  let cnt = aux 0 in
  print_terrain terrain;
  Printf.printf "Part One: %d\n" cnt

let _ =
  let lines = get_lines file in
  let minx, maxx, miny, maxy = minmax_terrain lines in
  let maxy = maxy + 2 in
  let minx = min minx (500 - maxy)
  and maxx = max maxx (500 + maxy) in
  let terrain =
    build_terrain (minx, maxx, miny, maxy) lines
  in
  for x = minx to maxx do
    terrain.(maxy - miny).(x - minx) <- '#'
  done;
  let rec aux cnt =
    if terrain.(0 - miny).(500 - minx) = '.' then (
      assert (drop_once terrain minx miny);
      aux (cnt + 1))
    else cnt
  in
  let cnt = aux 0 in
  print_terrain terrain;
  Printf.printf "Part Two: %d\n" cnt
