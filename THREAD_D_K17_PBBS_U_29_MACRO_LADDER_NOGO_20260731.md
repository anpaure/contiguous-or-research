# K17 PBBS-U Johnson macro search: exact 29-seed no-go

## 1. Scope and verdict

Let the frozen PBBS-U first-occurrence atlas be

```text
scratch/k17_pbbs_u.fragments
SHA-256 8db7db58a697171a7440fbd1c2333c782947737079530470b482a971948e9944
```

and let the 29 prefix/literal/suffix repairs be the rows of

```text
scratch/k17_pbbs_u_johnson_macro_candidates_20260731.tsv
SHA-256 adcf180e16d5a3a3a4e2313c46a62892c9165abb0e8be217714856e30775b98c
```

Each repaired atlas has 763 fragments partitioning the 5,005 rank-nine
masks.  It contains 4,242 fixed Johnson edges, whose rank-eight
intersections are distinct, and no fragment contains a coordinate factor
`010` or `0110`.

**Theorem 1.1.** None of these 29 repaired atlases can be ordered and
oriented as a Johnson path which simultaneously

1. uses 5,004 distinct rank-eight intersection colours;
2. covers every mask of rank at least ten by a consecutive union; and
3. has no internal positive coordinate run of length one or two.

This is a complete, solver-free no-go for the 29 frozen macro rows.  It is
not a no-go for another duplicate-occurrence selection, a different PBBS
re-cutting, or an unrestricted U-sector construction.

## 2. Exact endpoint-ladder bound

Suppose distinct rank-nine masks \(W_1,\ldots,W_m\subseteq T\) form an
inclusion-minimal interval with union \(T\), where \(|T|=9+d\).
Put \(C_i=T\setminus W_i\), so every \(C_i\) is a \(d\)-subset and

\[
 \bigcap_{i=1}^m C_i=\varnothing.
\]

If \(m>2\), minimality gives nonempty sets

\[
 A=\bigcap_{i=1}^{m-1}C_i,
 \qquad
 B=\bigcap_{i=2}^{m}C_i.
\]

They are disjoint, and every interior \(C_i\), \(2\le i\le m-1\), contains
\(A\cup B\).  The \(C_i\) are distinct, hence

\[
 m-2\le {9+d-|A\cup B|\choose d-|A\cup B|}
       \le {9+d-2\choose d-2}.
\]

For \(d=1\), two disjoint nonempty subsets cannot both lie in a singleton.
Consequently inclusion-minimal witnesses have at most

\[
 2,\quad 3,\quad 12
\]

cells at ranks 10, 11, and 12 respectively.  These are cell bounds, not
fixed edge-width guesses.  The replay enumerates windows beginning and
ending inside fragments and traverses only legal Johnson seams between
them, so the census is lossless.

For a missing rank-ten target \(T\), the statement simplifies further.  A
cross-fragment witness contains a seam between two distinct rank-nine
subsets of \(T\); those endpoints are coatoms of \(T\), so their union is
exactly \(T\).  Thus an empty seam-provider row is an immediate obstruction.

## 3. Exhaustive decision tree

The target-restricted replay gives the following exact partition.

* Twenty-six seeds have a rank-ten hole with no endpoint seam which is
  Johnson, uses an intersection colour outside the 4,242-colour internal
  palette, and avoids a sealed `010`/`0110` factor across its two incident
  fragments.
* Seeds 10 and 20 survive every individual rank-ten provider row.  Both have
  rank-eleven hole `0x23ff`, but the complete at-most-three-cell ladder
  catalogue for that target is empty.
* Seed 24, with macro

  ```text
  (x,y,z) = (0x20ff,0x21f7,0x61f6),
  ```

  is the only remaining branch.  Its exact deeper ladder counts are

  ```text
  0x23ff : 2
  0x27ff : 22
  0x33f7 : 46
  0x68ff : 2
  0x78ff : 4
  ```

  Here the rank-twelve catalogues use the proved twelve-cell limit.

Rows already killed by an empty rank-ten row are not sent to a deeper
model.  This early termination is part of the complete stratified search,
not an omitted branch.

## 4. The seed-24 orientation cut

Number seed 24's physical fragments from 0 through 762, with 762 the added
macro.  Its only `0x23ff` witnesses are

```text
0x03fd, 0x01ff, 0x20ff
0x20ff, 0x01ff, 0x03fd.
```

Their crossing seams are, respectively,

```text
F0(forward)   -> F762(forward)
F762(reverse) -> F0(reverse).
```

Thus every `0x23ff` witness forces

\[
 o(F_0)\oplus o(F_{762})=0.                 \tag{4.1}
\]

The missing rank-ten target `0x60ff` also has exactly two providers:

```text
0x607f, 0x20ff
0x20ff, 0x607f.
```

They require

```text
F0(reverse)   -> F762(forward)
F762(reverse) -> F0(forward),
```

and therefore force

\[
 o(F_0)\oplus o(F_{762})=1.                 \tag{4.2}
\]

Equations (4.1) and (4.2) are incompatible.  All four provider-pair choices
fail before endpoint degree, colour all-difference, subtour, or Hamilton
completion constraints are needed.  This closes the last seed.

## 5. Residence and staircase scope

The `010`/`0110` test is exact for internal positive runs of lengths one and
two in the standalone 5,005-cell U word.  Pairwise seam filtering alone
would not be sufficient for a positive construction, because a forbidden
factor can cross two or three seams through short fragments; the full path
model would need the four-state trace automaton or exact short-chain clauses.

This theorem does **not** certify or refute the final four-sector K17
staircase.  After embedding U among the other sectors, endpoint collars and
length-three starts still enter the global condition

\[
 \rho_1+\rho_2+\rho_3\le 7401.
\]

No all-K17 or unrestricted-PBBS conclusion is claimed.

## 6. Reproducible audit

```bash
python3 scratch/threadD_verify_k17_pbbs_u_29macro_ladder_nogo_20260731.py \
  --output scratch/threadD_k17_pbbs_u_29macro_ladder_nogo_20260731.audit.json
```

The verifier independently reconstructs all 29 atlases and all decisive
target-restricted seam/ladder catalogues.  A byte-identical second replay was
also performed.

```text
verifier SHA-256  b07d6b198866ab874948a77b5f2322a45897e4138c2c85a9a7a775a1493ff42c
audit SHA-256     eb999f6771835225ec6d12428dbda88b98ff03c916a200282492a515155c65e6
payload SHA-256   8b68129171914949c0253fa3262e07f3eb908e9fb01ed60c694303111e4d1d57
runtime           0.48 seconds
maximum RSS       46,678,016 bytes
```

No H100 solve was launched: the finite provider cut makes a Hamilton solver
unnecessary, and the server was CPU/swap saturated during this audit.
