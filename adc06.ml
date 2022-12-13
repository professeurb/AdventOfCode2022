(* let file = "test06_4.txt" *)
let file = "input06.txt"

let rec tester s a j b c =
  if j = a then if b = c then c else tester s a b (b + 1) c
  else if s.[j] = s.[b] then
    tester s j (j + 1) (j + 2) (c + j - a)
  else tester s a (j - 1) b c

let _ =
  let f = open_in file in
  let l = input_line f in
  close_in f;
  Printf.printf "Part One : %d\n" (tester l (-1) 0 1 4);
  Printf.printf "Part Two : %d\n" (tester l (-1) 0 1 14)
