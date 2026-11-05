let data =
  let file = open_in "1.in" in
  Fun.protect
    ~finally:(fun () -> close_in file)
    (fun () -> really_input_string file (in_channel_length file))
  |> String.trim

let lines = if data = "" then [] else String.split_on_char '\n' data

let graph =
  let graph = Hashtbl.create 1024 in
  List.iter
    (fun line ->
      match String.split_on_char ':' line with
      | [ left; right ] ->
          let nbrs = String.split_on_char ',' right in
          Hashtbl.replace graph left nbrs
      | _ -> failwith ("Invalid line: " ^ line))
    lines;
  graph

let seen : (string, unit) Hashtbl.t = Hashtbl.create 1024
let bfs = [ "NULL" ]

let rec process bfs seen graph =
  match bfs with
  | [] -> Hashtbl.length seen - 1
  | cur :: rest ->
      if Hashtbl.mem seen cur then process rest seen graph
      else (
        Hashtbl.replace seen cur ();
        match Hashtbl.find_opt graph cur with
        | Some nbrs -> process (nbrs @ rest) seen graph
        | None -> process rest seen graph)

let () = Printf.printf "%d\n" (process bfs seen graph)

(* **************************************************** *)

let data =
  let file = open_in "2.in" in
  Fun.protect
    ~finally:(fun () -> close_in file)
    (fun () -> really_input_string file (in_channel_length file))
  |> String.trim

let lines = if data = "" then [] else String.split_on_char '\n' data

let graph =
  let graph = Hashtbl.create 1024 in
  List.iter
    (fun line ->
      match String.split_on_char ':' line with
      | [ left; right ] ->
          let nbrs = String.split_on_char ',' right in
          Hashtbl.replace graph left nbrs
      | _ -> failwith ("Invalid line: " ^ line))
    lines;
  graph

let rec process2 bfs seen graph =
  match bfs with
  | [] -> if Hashtbl.mem seen "NULL" then 1 else 0
  | cur :: rest ->
      if Hashtbl.mem seen cur then process2 rest seen graph
      else (
        Hashtbl.replace seen cur ();
        match Hashtbl.find_opt graph cur with
        | Some nbrs ->
            let unseen =
              List.filter (fun node -> not (Hashtbl.mem seen node)) nbrs
            in
            process2 (unseen @ rest) seen graph
        | None -> process2 rest seen graph)

let ans =
  Hashtbl.fold
    (fun key _ acc ->
      match key with
      | "NULL" -> acc
      | _ ->
          let bfs = [ key ] in
          let seen : (string, unit) Hashtbl.t = Hashtbl.create 1024 in
          let ans = process2 bfs seen graph in
          acc + ans)
    graph 0

let () = Printf.printf "%d\n" ans

(* ************************************************* *)

let data =
  let file = open_in "3.in" in
  Fun.protect
    ~finally:(fun () -> close_in file)
    (fun () -> really_input_string file (in_channel_length file))
  |> String.trim

let lines = if data = "" then [] else String.split_on_char '\n' data

let graph =
  let graph = Hashtbl.create 1024 in
  List.iter
    (fun line ->
      match String.split_on_char ':' line with
      | [ left; right ] ->
          let nbrs = String.split_on_char ',' right in
          Hashtbl.replace graph left nbrs
      | _ -> failwith ("Invalid line: " ^ line))
    lines;
  graph

let rec process3 bfs seen graph =
  match bfs with
  | [] -> (
      match
        ( Hashtbl.mem seen "NULLv1",
          Hashtbl.mem seen "NULLv2",
          Hashtbl.mem seen "NULLv3" )
      with
      | true, true, _ | true, _, true | _, true, true -> 1
      | _ -> 0)
  | cur :: rest ->
      if Hashtbl.mem seen cur then process3 rest seen graph
      else (
        Hashtbl.replace seen cur ();
        match Hashtbl.find_opt graph cur with
        | Some nbrs ->
            let unseen =
              List.filter (fun node -> not (Hashtbl.mem seen node)) nbrs
            in
            process3 (unseen @ rest) seen graph
        | None -> process3 rest seen graph)

let ans =
  Hashtbl.fold
    (fun key _ acc ->
      match key with
      | "NULLv1" | "NULLv2" | "NULLv3" -> acc
      | _ ->
          let bfs = [ key ] in
          let seen : (string, unit) Hashtbl.t = Hashtbl.create 1024 in
          let ans = process3 bfs seen graph in
          acc + ans)
    graph 0

let () = Printf.printf "%d\n" ans
