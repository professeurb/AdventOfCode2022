(* ocamlfind ocamlopt -package Brulib -linkpkg adc23.ml -o adc23 *)

open Brulib

(* let file = "test23.txt" *)
(* let file = "test23_2.txt" *)
let file = "input23.txt"

let happend h k v =
  match Hashtbl.find_opt h k with
  | None -> Hashtbl.add h k [ v ]
  | Some l -> Hashtbl.replace h k (v :: l)

let print_map map =
  let xmin = Hashset.fold (fun m (x, _) -> min m x) max_int map
  and xmax = Hashset.fold (fun m (x, _) -> max m x) min_int map
  and ymin = Hashset.fold (fun m (_, y) -> min m y) max_int map
  and ymax =
    Hashset.fold (fun m (_, y) -> max m y) min_int map
  in
  for y = ymin to ymax do
    for x = xmin to xmax do
      if Hashset.mem map (x, y) then print_char '#'
      else print_char '.'
    done;
    print_newline ()
  done

let _ =
  let elf_map = Hashset.init () and y = ref 0 in
  Gen.(
    of_file file
    |> map (fun v ->
           incr y;
           (!y, v))
    |> iter (fun (y, s) ->
           for x = 0 to String.length s - 1 do
             if s.[x] = '#' then Hashset.add elf_map (x, y)
           done));
  let dirs =
    [| [ 0; 1; 2 ]; [ 4; 5; 6 ]; [ 0; 6; 7 ]; [ 2; 3; 4 ] |]
  and first_dir = ref 3 in
  let one_round map =
    (* print_map map; *)
    (* print_newline (); *)
    first_dir := (1 + !first_dir) mod 4;
    let h = Hashtbl.create (Hashset.length map) in
    Hashset.iter
      (fun (x, y) ->
        let presence =
          Array.map (Hashset.mem map)
            [|
              (x - 1, y - 1);
              (x, y - 1);
              (x + 1, y - 1);
              (x + 1, y);
              (x + 1, y + 1);
              (x, y + 1);
              (x - 1, y + 1);
              (x - 1, y);
            |]
        and future_pos =
          [| (x, y - 1); (x, y + 1); (x - 1, y); (x + 1, y) |]
        in
        if Array.for_all not presence then happend h (x, y) (x, y)
        else if
          List.for_all
            (fun i -> not presence.(i))
            dirs.(!first_dir)
        then happend h future_pos.(!first_dir) (x, y)
        else if
          List.for_all
            (fun i -> not presence.(i))
            dirs.((!first_dir + 1) mod 4)
        then happend h future_pos.((!first_dir + 1) mod 4) (x, y)
        else if
          List.for_all
            (fun i -> not presence.(i))
            dirs.((!first_dir + 2) mod 4)
        then happend h future_pos.((!first_dir + 2) mod 4) (x, y)
        else if
          List.for_all
            (fun i -> not presence.(i))
            dirs.((!first_dir + 3) mod 4)
        then happend h future_pos.((!first_dir + 3) mod 4) (x, y)
        else happend h (x, y) (x, y))
      map;
    let hs = Hashset.init () and change = ref false in
    Hashtbl.iter
      (fun k l ->
        match l with
        | [ v ] ->
            if k <> v then change := true;
            Hashset.add hs k
        | _ -> List.iter (fun v -> Hashset.add hs v) l)
      h;
    if !change then Some hs else None
  in
  let rec aux1 m c =
    if c = 0 then m
    else
      match one_round m with
      | None -> m
      | Some m' -> aux1 m' (c - 1)
  in

  let final_map = aux1 elf_map 10 in
  let xmin =
    Hashset.fold (fun m (x, _) -> min m x) max_int final_map
  and xmax =
    Hashset.fold (fun m (x, _) -> max m x) min_int final_map
  and ymin =
    Hashset.fold (fun m (_, y) -> min m y) max_int final_map
  and ymax =
    Hashset.fold (fun m (_, y) -> max m y) min_int final_map
  in
  Printf.printf "Part One: %d\n"
    (((ymax - ymin + 1) * (xmax - xmin + 1))
    - Hashset.length final_map);
  print_map final_map;
  (* Part Two *)
  let rec aux2 m c =
    match one_round m with
    | None -> c
    | Some m' -> aux2 m' (c + 1)
  in
  first_dir := 3;
  Printf.printf "Part Two: %d\n" (aux2 elf_map 1)
