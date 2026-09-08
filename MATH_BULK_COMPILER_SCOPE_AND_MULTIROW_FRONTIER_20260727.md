# Scope of the bulk compiler and the correct multirow frontier

Date: 2026-07-27

## 1. The scope correction

Put

\[
r=\lceil k/2\rceil,
\qquad W=\binom kr,
\qquad
\Lambda=\sum_{a=1}^{r-1}\binom ka,
\]

and let `d=d(k)` be least with

\[
\Lambda\le dW+\binom{d+1}{2}.
\]

The first-derivative compiler in
`MATH_BULK_PCSH_COMPILER_20260727.md` puts every mask of rank at most

\[
s=r-d
\]

literally into the base row.  This is a valid and particularly clean
compiler whenever its Hall system is feasible.  It is **not** a
dimension-uniform normal form, because it first requires the elementary
capacity inequality

\[
L_0(k):=\sum_{a=1}^{s}\binom ka\le W+d.
\tag{1.1}
\]

The failure is already visible at `k=9`:

\[
k=9,quad d=2,quad s=3,quad L_0=9+36+84=129>128=W+d.
\]

The known optimal word handles the unique excess rank-three mask in row
`D^1`, so this is a limitation of the literal-base-row compiler, not of the
exact formula.

Some representative values are:

| `k` | `d` | `s` | `L_0/(W+d)` |
|---:|---:|---:|---:|
| 9 | 2 | 3 | 1.0238 |
| 11 | 3 | 3 | 0.4968 |
| 13 | 3 | 4 | 0.6353 |
| 30 | 3 | 12 | 1.2515 |
| 100 | 6 | 44 | 1.7041 |
| 500 | 14 | 236 | 3.1854 |

The nonmonotonic small cases come from the integer jumps of `d`; they do not
alter the asymptotic conclusion.

## 2. Asymptotic impossibility of a literal base row

For both parities,

\[
W=(1+o(1))2^k\sqrt{\frac{2}{\pi k}},
\qquad
d=(1+o(1))\sqrt{\frac{\pi k}{8}}.
\tag{2.1}
\]

If `X` is binomial `Bin(k,1/2)`, then

\[
\frac{s-k/2}{\sqrt{k}/2}
\longrightarrow -\sqrt{\frac\pi2}.
\]

The central limit theorem therefore gives

\[
\begin{aligned}
L_0(k)
&=(1+o(1))2^k
  \Phi\!\left(-\sqrt{\frac\pi2}\right),\\
\frac{L_0(k)}W
&=(1+o(1))
  \Phi\!\left(-\sqrt{\frac\pi2}\right)
  \sqrt{\frac{\pi k}{2}}
  =\Theta(\sqrt{k}).
\end{aligned}
\tag{2.2}
\]

Thus (1.1) eventually fails by an unbounded factor.  The same conclusion
holds if the rank-`s` layer is reserved first: the number of strict-low
targets is still `Theta(sqrt(k) W)`.

Consequently:

> The first-derivative collapse is an exact finite/special-regime compiler
> and a useful terminal module, but it cannot be the uniform proof of
> `nu(k)=B(k)`.

## 3. The required multirow arithmetic

The `d` rows below a flat central row have capacities

\[
c_j=W+d-j\qquad(0\le j<d),
\]

whose sum is

\[
\sum_{j<d}c_j=dW+\binom{d+1}{2}=\Lambda+e.
\]

Here `e` is exactly the rank slack.  If `u_j` lower masks receive their first
witness in row `j`, the complete arithmetic condition is

\[
0\le u_j\le c_j,
\qquad
\sum_{j<d}u_j=\Lambda.
\tag{3.1}
\]

As proved in `MATH_CAPACITY_ORDERED_OR_PASCAL_QUANTILES_20260727.md`, a
rank-monotone schedule may split at most one rank at every row boundary.
There is no additional rank-count obstruction.  What remains is geometric:
the assigned cells in different rows overlap in the physical word.

## 4. Exact geometric criterion

There is a compact formulation which treats all rows at once.  Assign to
every nonempty mask `S` a distinct physical interval `I_S` in a word of
length `n`.  For every position `i`, put

\[
E_i=\bigcap_{S:\ i\in I_S}S,
\tag{4.1}
\]

where an empty intersection is `[k]`.

### Theorem 4.1 (full interval-label realization)

The prescribed intervals are simultaneously realizable by a nonzero set
word `A` with

\[
\bigcup_{i\in I_S}A_i=S
\qquad(S\ne\varnothing)
\tag{4.2}
\]

if and only if

\[
E_i\ne\varnothing\quad\text{for every }i,
\tag{4.3}
\]

and

\[
\bigcup_{i\in I_S}E_i=S
\quad\text{for every }S\ne\varnothing.
\tag{4.4}
\]

When these conditions hold, `A_i=E_i` is the entrywise maximal realization.

#### Proof

Any coordinate absent from a prescribed label `S` must be absent at every
position of `I_S`.  Therefore every realization satisfies `A_i subseteq
E_i`.  Nonzero entries force (4.3), and a positive coordinate of `S` can
occur on `I_S` only where it belongs to `E_i`, forcing (4.4).

Conversely take `A_i=E_i`.  Equation (4.1) excludes every coordinate not in
`S` throughout `I_S`, while (4.4) supplies every coordinate in `S` at least
once.  Thus (4.2) holds, and (4.3) makes the word nonzero.  □

Equivalently, for each coordinate `x`, define

\[
Z_x=[n]\setminus\bigcup_{S:\ x\notin S}I_S.
\]

Then every positive interval `I_S`, `x in S`, must meet `Z_x`, and the
`Z_x` must cover all physical positions.  This is exactly Theorem 3.1 of
`MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md`.

## 5. Correct general target

Within a flat-central normal form, a uniform proof of the exact formula now
requires one coupled object:

1. assign the `W` middle masks to the width-`d` central intervals;
2. inject all `Lambda` lower masks into the complete short band, distributed
   among rows according to (3.1), or any equivalent slack path;
3. assign upper masks to actual longer windows of the central chronology;
4. satisfy the coordinatewise realization conditions (4.3)--(4.4).

The universal-shadow rotor addresses items 1 and 3.  The bulk
first-derivative compiler solves an especially clean subcase of item 2, but
the general proof needs a **multirow OR--Pascal packing**, with rank cuts
allowed to pass through rows.

This restores the correct frontier:

\[
\boxed{
\text{global central rotor/upper shadows}
+
\text{multirow interval-label realization}.}
\]

The good-cut surplus-Hall problem remains useful for dimensions such as
`k=11` and as a terminal block in a future recursion.  It is not, by itself,
the asymptotic compiler gate.
