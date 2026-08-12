# Upper-q1 holes cannot be bypassed by a depth-3 compiler

Let `D` be the cyclic OR derivative,

\[
(DA)_i=A_i\cup A_{i+1},
\]

and suppose a factor word `A` has middle carrier

\[
T=D^3A.
\]

The following identity makes an upper-q1 hole of `T` fatal, independently
of how the lower compiler labels the entries of `A`.

## Fixed long-window identity

For every cyclic start `s` and every `L >= 4`,

\[
\boxed{
  \bigcup_{j=0}^{L-1}A_{s+j}
  =
  \bigcup_{j=0}^{L-4}T_{s+j}.
}
\]

Indeed, expanding each

\[
T_{s+j}=A_{s+j}\cup A_{s+j+1}\cup A_{s+j+2}\cup A_{s+j+3}
\]

shows that the right side contains exactly the entry positions
`s,...,s+L-1`.

If `P` is the maximal erosion used by the sandwich compiler, so that
`D^3P=T` and `A <= P`, the same calculation gives

\[
  \bigcup_{j=0}^{L-1}A_{s+j}
  =
  \bigcup_{j=0}^{L-1}P_{s+j}.
\]

Thus every compiler window of length at least four is already fixed by the
middle carrier.  There is no upper-side labeling freedom at these lengths.

## Rank-8 corollary for k=13

Here every `T_i` has rank seven and consecutive carrier vertices are
distinct Johnson neighbours.

- A window of at most four entries is contained in a length-four window,
  whose union is one `T_i`; it therefore has rank at most seven.
- A length-five entry window has union

  \[
  T_s\cup T_{s+1},
  \]

  exactly an upper-q1 carrier shadow.
- A longer entry window contains its first length-five union, already of
  rank eight.  If the longer union still has rank eight, it must equal that
  same adjacent union.

Consequently

\[
\boxed{
\{\text{rank-8 ORs of consecutive entry windows of }A\}
=
\{T_i\cup T_{i+1}:i\in\mathbb Z_W\}.
}
\]

So a missing upper-q1 target of the carrier cannot be supplied by a shorter
or longer compiler window.  This remains true after a cyclic cut: cutting can
delete wraparound windows but cannot create a new cyclic window value.

## Audit of the residence-perfect one-hole carrier

For

`scratch/k13_res0_onehole_round6.certificate.json`, the only carrier hole is
the upper-q1 orbit with representative `1499` (13 physical rank-8 masks).
The maximal erosion has rank profile `4^1716`.

For each of the 13 rotations of `1499`:

- no maximal-envelope window equals the target;
- no window of length 1 through 5 even contains the target;
- the first containing windows occur at length 6: there are 12, and every
  one has fixed rank-9 union, hence one forced extra coordinate;
- the containing counts at lengths 7, 8, 9, and 10 are respectively
  `46, 127, 261, 412`, but all are likewise fixed supersets.

The lower Hall audit passes with deficiency zero, and the SAT compiler covers
the entire lower ideal, but its final full-word audit misses exactly the same
13 masks.  This is forced by the identity above, not by the compiler's choice
of sandwich core.

Artifacts:

- carrier: `scratch/k13_res0_onehole_round6.certificate.json`
- lower Hall audit: `scratch/k13_res0_onehole_round6.hall.json`
- compiled word: `scratch/k13_res0_onehole_round6.word.json`

