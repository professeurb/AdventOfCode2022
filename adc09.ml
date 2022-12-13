#require "brulib"

open Brulib

(* let file = "test09.txt" *)
let file = "input09.txt"

let follow_once (tx, ty) (hx, hy) =
  let dx = tx - hx and dy = ty - hy in
  if abs dx = 2 || abs dy = 2 then
    (hx + (dx / 2), hy + (dy / 2))
  else (hx + dx, hy + dy)

let dir = function
  | 'L' -> (-1, 0)
  | 'R' -> (1, 0)
  | 'U' -> (0, 1)
  | 'D' -> (0, -1)
  | _ -> failwith "Wrong direction"

let follow t = Gen.genfold follow_once (0, 0) t

let data () =
  Gen.scan_file file "%c %d" (fun c d -> (dir c, d))

let head () =
  Gen.of_fun (fun yield ->
      let x = ref 0 and y = ref 0 in
      yield (!x, !y);
      Gen.iter
        (fun ((dx, dy), amp) ->
          for _ = 1 to amp do
            x := !x + dx;
            y := !y + dy;
            yield (!x, !y)
          done)
        (data ()))

let count t =
  let h = Hashtbl.create 100 in
  Gen.iter (fun v -> Hashtbl.replace h v ()) t;
  Hashtbl.length h

let _ =
  Printf.printf "Part One: %d\n"
    (Gen.(head () |> follow) |> count)

let _ =
  let pos = ref (head ()) in
  for _ = 1 to 9 do
    pos := follow !pos
  done;
  Printf.printf "Part Two: %d\n" (count !pos)
