#require "brulib"

open Brulib

(* let file = "test16.txt" *)
let file = "input16.txt"

let rec process_list s =
  if String.length s = 2 then [ s ]
  else
    let l = String.length s in
    String.sub s (l - 2) 2
    :: process_list (String.sub s 0 (l - 4))

let get_data file =
  let flow = Hashtbl.create 10
  and neigh = Hashtbl.create 10
  and numbers = Hashtbl.create 10
  and cnt = ref 0 in
  Gen.(
    scan_file file
      "Valve %s has flow rate=%d; %_s %_s to %_s %s@\t"
      (fun x y z -> (x, y, process_list z))
    |> iter (fun (x, y, z) ->
           Hashtbl.add flow x y;
           Hashtbl.add neigh x z;
           Hashtbl.add numbers x !cnt;
           incr cnt));
  (numbers, neigh, flow)

let make_graph numbers neigh =
  let n = Hashtbl.length numbers in
  let g = Array.make_matrix n n max_int in
  for i = 0 to n - 1 do
    g.(i).(i) <- 0
  done;
  Hashtbl.iter
    (fun valve voisins ->
      List.iter
        (fun voisin ->
          g.(Hashtbl.find numbers valve).(Hashtbl.find
                                            numbers voisin) <-
            1)
        voisins)
    neigh;
  (* Floyd-Warshall *)
  for k = 0 to n - 1 do
    for i = 0 to n - 1 do
      for j = 0 to n - 1 do
        if g.(i).(k) < max_int && g.(k).(j) < max_int then
          g.(i).(j) <- min g.(i).(j) (g.(i).(k) + g.(k).(j))
      done
    done
  done;
  g

let make_weights numbers flow =
  let n = Hashtbl.length numbers in
  let weights = Array.make n 0 in
  Hashtbl.iter
    (fun k n -> weights.(n) <- Hashtbl.find flow k)
    numbers;
  weights

let _ =
  let nums, neighs, flows = get_data file in
  let g = make_graph nums neighs
  and w = make_weights nums flows in
  let n = Array.length g in
  let maxi = ref 0
  and seen = Array.make n false
  and aa = Hashtbl.find nums "AA" in
  for i = 0 to n - 1 do
    if w.(i) = 0 then seen.(i) <- true
  done;
  let rec dfs1 vert time score remain =
    if score > !maxi then maxi := score;
    if time >= 0 then
      for v1' = 0 to n - 1 do
        if not seen.(v1') then
          let time' = time - (1 + g.(vert).(v1')) in
          if score + (time' * remain) > !maxi then (
            seen.(v1') <- true;
            dfs1 v1' time'
              (score + (w.(v1') * time'))
              (remain - w.(v1'));
            seen.(v1') <- false)
      done
  in
  dfs1 aa 30 0 (Array.fold_left ( + ) 0 w);
  Printf.printf "Part One: %d\n" !maxi;
  for i = 0 to n - 1 do
    seen.(i) <- w.(i) = 0
  done;
  maxi := 0;
  let rec dfs2 v1 t1 v2 t2 score total nb =
    if t1 < t2 then dfs2 v2 t2 v1 t1 score total nb
    else (
      if t1 >= 0 && t2 >= 0 && score > !maxi then
        maxi := score;
      if t1 >= 0 then (
        let min_t1' = ref t1 in
        for v1' = 0 to n - 1 do
          if not seen.(v1') then
            let t1' = t1 - (1 + g.(v1).(v1')) in
            if score + (total * t1') >= !maxi then (
              seen.(v1') <- true;
              min_t1' := min !min_t1' t1';
              dfs2 v1' t1' v2 t2
                (score + (w.(v1') * t1'))
                (total - w.(v1'))
                (nb - 1);
              seen.(v1') <- false)
        done;
        if t2 - (2 * nb) >= !min_t1' then
          (* Le détail qui m'a embété *)
          (* print_endline "*"; *)
          dfs1 v2 t2 score total))
  in
  dfs2 aa 26 aa 26 0
    (Array.fold_left ( + ) 0 w)
    (Array.fold_left
       (fun s b -> if b then s else s + 1)
       0 seen);
  Printf.printf "Part Two: %d\n" !maxi
