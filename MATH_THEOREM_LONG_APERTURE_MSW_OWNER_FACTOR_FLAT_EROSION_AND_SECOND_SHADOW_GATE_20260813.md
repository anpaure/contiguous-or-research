# Long-aperture MSW wreaths give an exact owner factor with flat erosion; the first unsolved deck is the second shadow

**Date:** 2026-08-13  
**Status:** unconditional owner-factor and flat-antecedent theorem; exact
deck census and literal first obstruction  
**Convention:** `q=d+1` is the required flat residence/erosion length;
`r` is the middle rank, and `q <= r-1`

## 1. Odd ground: exact owners and exact immediate lowers

Let

\[
 k=2r-1,\qquad R=r,\qquad q\le r-1.                \tag{1.1}
\]

The M\"utze--Standke--Wiechert theorem factors

\[
 KG(2r-1,r-1)                                      \tag{1.2}
\]

into minimum odd cycles.  Every such cycle is the family of all cyclic
`(r-1)`-windows in some cyclic order

\[
 \sigma=(x_0,\ldots,x_{2r-2}).                     \tag{1.3}
\]

Complementing those windows gives the family of all cyclic `r`-windows in
the same order, after a harmless phase shift.  Write the resulting owner
component as

\[
 O_i=I_i^r(\sigma),\qquad i\in\mathbb Z_{2r-1}.    \tag{1.4}
\]

### Theorem 1.1 (odd long-aperture factor)

The components (1.4), over one MSW factor, have the following properties.

1. They partition `binom([k],r)` exactly.
2. Every component is an owner-simple closed Johnson cycle.
3. Its maximal flat `q`-antecedent may be written

   \[
   A_i=I_i^{r-q+1}(\sigma),                         \tag{1.5}
   \]

   and satisfies

   \[
   \bigcup_{j=0}^{q-1}A_{i+j}=O_i.                 \tag{1.6}
   \]

4. Every coordinate has owner trace `1^r0^(r-1)`, up to cyclic shift.
   Hence the components are positively and negatively resident at
   threshold `q`.
5. The complete immediate-lower deck is exact:

   \[
   \bigsqcup_\rho
   \{O_i^\rho\cap O_{i+1}^\rho:i\in\mathbb Z_k\}
   =\binom{[k]}{r-1}.                               \tag{1.7}
   \]

### Proof

The MSW cycles partition the `(r-1)`-sets.  The minimum-odd-cycle normal
form identifies each cycle with all `(r-1)`-windows of (1.3).
Complementation is a bijection from rank `r-1` to rank `r`, proving the
owner partition.  Consecutive `r`-windows differ by one deletion and one
insertion, so (1.4) is a simple Johnson cycle.

The union of `q` consecutive intervals of length `r-q+1` is the interval
of length `r`, proving (1.6).  A coordinate lies in `r` consecutive
`r`-windows and outside the other `r-1`; (1.1) proves both residence
inequalities.  Finally,

\[
 O_i\cap O_{i+1}=I_{i+1}^{r-1}(\sigma).            \tag{1.8}
\]

These are exactly the original MSW wreath vertices, once each globally,
which proves (1.7). \(\square\)

The number of components is

\[
 \frac1{2r-1}\binom{2r-1}{r-1}
 =\operatorname{Cat}_{r-1}.                        \tag{1.9}
\]

Thus this is an integral exact owner factor, not a fractional carousel or
a fixed-core decomposition.

## 2. The full odd interval-deck census

For `ell >= 1`, as long as the resulting interval is proper,

\[
 Z_{i,\ell}:=\bigcup_{j=0}^{\ell-1}A_{i+j}
 =I_i^{t}(\sigma),
 \qquad t=r-q+\ell.                                \tag{2.1}
\]

Consequently one component has `2r-1` distinct targets at every proper
rank `t`.  Across the whole factor the number of endpoint occurrences at
each such rank is

\[
 W_{\rm odd}:=\binom{2r-1}{r}.                     \tag{2.2}
\]

The average multiplicity on rank `t` is therefore

\[
 \mu_t=\frac{W_{\rm odd}}{\binom{2r-1}{t}}.        \tag{2.3}
\]

The proper range is `1 <= t <= 2r-2`, equivalently
`ell <= r+q-2`.  At the next width

\[
 \ell_{\rm full}=r+q-1,                            \tag{2.3a}
\]

every endpoint interval equals the full ground `[k]`.  Thus there are
`W_(odd)` endpoint occurrences but only `Cat_(r-1)` component-level
incidences with the unique full target.  This is the same full-period
normalization distinction as in the shorter rail catalogue.

Within each component every proper deck is simple.  Globally, only the
owner rank `r` and immediate-lower rank `r-1` are forced exact by MSW.
Complementation inside the cyclic order gives

\[
 \overline{I_i^t}=I_{i+t}^{2r-1-t}.               \tag{2.4}
\]

Thus coverage of rank `t` is equivalent to coverage of rank `2r-1-t`.

At the immediate-upper rank,

\[
 O_i\cup O_{i+1}=I_i^{r+1}(\sigma),                \tag{2.5}
\]

and (2.4) identifies its coverage with coverage of all rank-`(r-2)`
windows in the MSW cyclic orders.  The scalar ledger is

\[
 \frac{W_{\rm odd}}{\binom{2r-1}{r+1}}
 =\frac{r+1}{r-1}.                                 \tag{2.6}
\]

Hence there is enough total mass, but only a relative surplus `2/(r-1)`.
Surjectivity of this second-shadow row is not a consequence of the MSW
owner factor.  If every immediate-upper occurrence were instead declared
a capacity-one compulsory ticket, global simplicity would be impossible:
the forced multiplicity excess is

\[
 W_{\rm odd}-\binom{2r-1}{r+1}
 =\frac{2W_{\rm odd}}{r+1}.                        \tag{2.7}
\]

Thus the proof-safe interpretation is exact immediate-lower ownership plus
optional/designated upper witnesses.  A globally simple complete upper row
cannot be part of this long-aperture factor.

## 3. Even ground: a fixed-coordinate split

Now let

\[
 k=2r,qquad R=r,qquad q\le r-1,                  \tag{3.1}
\]

fix `x in [k]`, and put `Y=[k]\setminus{x}`, so `|Y|=2r-1`.
Take one MSW central-wreath factor of `binom(Y,r-1)`.  For a wreath order
`sigma`, form the two owner components

\[
 X_i=\{x\}\cup I_i^{r-1}(\sigma),
 \qquad
 Y_i=Y\setminus I_i^{r-1}(\sigma).                \tag{3.2}
\]

After a phase shift the second component is the all-start `r`-window deck.

### Theorem 3.1 (even split owner factor)

The components (3.2) partition `binom([k],r)` exactly.  They are simple
closed Johnson cycles and have flat `q`-antecedents

\[
 A_i^x=\{x\}\cup I_i^{r-q}(\sigma),
 \qquad
 A_i^0=I_{i+r-1}^{r-q+1}(\sigma).                 \tag{3.3}
\]

The `x`-shore toggle traces are `1^(r-1)0^r`, with `x` constantly one;
the zero-shore traces are `1^r0^(r-1)`.  Thus both shores are biresident
at threshold `q`.

### Proof

Adding `x` to the MSW partition gives every rank-`r` owner containing `x`
exactly once.  Complementing in `Y` gives every rank-`r` owner avoiding
`x` exactly once.  The two classes are disjoint and exhaust the owner
layer.  Johnson adjacency and the trace claims follow from consecutive
windows.  Taking the union of `q` consecutive sets in (3.3) gives (3.2),
proving flat inversion. \(\square\)

There are `Cat_(r-1)` components on each shore and

\[
 2(2r-1)\operatorname{Cat}_{r-1}
 =\binom{2r}{r}                                    \tag{3.4}
\]

owners in total.

## 4. The full even split-deck census

At source width `ell`, put

\[
 t=r-q+\ell.                                       \tag{4.1}
\]

For proper intervals the two decks are

\[
 Z^x_{i,\ell}
 =\{x\}\cup I_i^{t-1}(\sigma),
 \qquad
 Z^0_{i,\ell}
 =I_{i+r-1}^{t}(\sigma).                           \tag{4.2}
\]

Each shore has

\[
 W_0:=\binom{2r-1}{r-1}                            \tag{4.3}
\]

endpoint occurrences at every proper width.  The target counts and average
multiplicities at rank `t` are

\[
 \begin{array}{c|c|c}
 \text{shore}&\text{number of named targets}&\text{average load}\\ \hline
 x\in Z&\binom{2r-1}{t-1}&
          W_0/\binom{2r-1}{t-1}\\[1mm]
 x\notin Z&\binom{2r-1}{t}&
          W_0/\binom{2r-1}{t}.
\end{array}                                       \tag{4.4}
\]

On the zero-shore the first full toggle interval occurs at
`ell=r+q-1`, when every endpoint gives the one target `Y` of rank `k-1`.
On the `x`-shore it occurs at `ell=r+q`, when every endpoint gives `[k]`.
At either boundary, distinct endpoint occurrences must again be collapsed
to one component-to-target incidence when only named coverage is counted.

The same-order complement identity pairs the `x`-shore width `ell` with
the zero-shore width `2q-ell`.

At the three central ranks the exact status is:

\[
\begin{array}{c|c|c}
\text{row}&x\text{-shore}&0\text{-shore}\\ \hline
r-1\text{ (immediate lower)}&
  \{x\}\cup I^{r-2}:\text{ second-shadow gate}&
  I^{r-1}:\text{ exact}\\
r\text{ (owner)}&
  \{x\}\cup I^{r-1}:\text{ exact}&
  I^r:\text{ exact}\\
r+1\text{ (immediate upper)}&
  \{x\}\cup I^r:\text{ exact}&
  I^{r+1}:\text{ second-shadow gate}.
\end{array}                                        \tag{4.5}
\]

The two gate entries are complements of each other.  Each has occurrence
ratio

\[
 \frac{W_0}{\binom{2r-1}{r-2}}
 =\frac{r+1}{r-1},                                 \tag{4.6}
\]

and forced excess `2W_0/(r+1)` if every occurrence is kept.  Therefore a
fixed-`x` split does **not** by itself give an exact complete
immediate-lower factor: only the lower targets avoiding `x` are certified.
The missing containing-`x` lower row is exactly the same second-shadow
surjectivity problem as the missing non-`x` upper row.

## 5. Exact conclusion

The long-aperture idea succeeds at its first advertised task:

\[
 \boxed{\text{MSW wreaths give an exact integral owner factor with a
 flat `q`-erosion in both parities.}}               \tag{5.1}
\]

For odd `k=2r-1`, it also gives the entire immediate-lower layer exactly.
For even `k=2r`, the fixed-coordinate split certifies only one half of the
immediate-lower layer.

The first unresolved deck is not an asymptotic count or residence issue.
It is the literal second-shadow condition

\[
 \boxed{
 \bigcup_{\rho\in\mathrm{MSW}}
 \{I_i^{r-2}(\sigma_\rho):i\in\mathbb Z_{2r-1}\}
 =\binom{[2r-1]}{r-2}.}                            \tag{5.2}
\]

with multiplicity allowed.  Its relative occurrence surplus tends to
zero.  MSW factorization alone does not prove (5.2), and global
capacity-one simplicity at this row is arithmetically impossible.

Accordingly this route removes the joint owner-rounding problem outright
on odd ground and removes it on both fixed-`x` owner shores on even ground.
It does not yet supply the all-width upper witnesses, the missing even
lower half, occurrence sockets, or cap routing.  Any use in the final
compiler must either prove (5.2), rethread the central wreath factor while
preserving its exact owner partition, or designate external backups for
the nonexact rows.
