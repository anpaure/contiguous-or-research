# The `B+2` two-stutter boundary fixes the owner palette, but leaves an arbitrary-width exterior grid

Date: 2026-08-01  
Lane: K, endpoint rotation / upper-ticket audit  
Status: exact positive owner and short-band theorem; exact arbitrary-width
residual decomposition; quadratic targetwise counterexample.  The stutters
reduce the first uncontrolled rows to two one-sided rays, but at longer
widths a two-sided grid survives.  Full upper preservation still needs a
prepared exterior-deck equality or a compound grid return.

## 0. Verdict

Let

\[
 C=A\cup B,\qquad F=\{f_1,\ldots,f_d\},\qquad
 U=C\cup F,                                                 \tag{0.1}
\]

and let the nonempty core stutter satisfy

\[
                         K\subseteq A\cap B.                 \tag{0.2}
\]

Put

\[
 Z=A\cup\{f_1\},\qquad T=B\cup\{f_d\},                    \tag{0.3}
\]

and use the two length-`d` collars

\[
\begin{aligned}
 Q^-&=(\{f_{d-1}\},\ldots,\{f_2\},K,Z),\\
 P^+&=(T,K,\{f_{d-1}\},\ldots,\{f_2\}).                   \tag{0.4}
\end{aligned}
\]

The proposed owner calculation is correct.  The `d` length-`d+1` windows
crossing `Q^-|P^+` are

\[
                 U,D_{d-1},D_{d-2},\ldots,D_2,U,
       \qquad D_j=U-\{f_j\}.                               \tag{0.5}
\]

Thus the two copies of `U` exactly use the two `B+2` surplus positions and
the `d-2` internal coatoms are squarefree.

If the old and new cuts literally carry the same two collars (0.4), every
crossing interval using at most `d` letters on each side is transported
address by address.  In particular every row of width at most `d+1`,
including the complete lower and owner band, is safe.

This does **not** close arbitrary-width upper coverage.  Beyond the collar,
the exact interface is

\[
             \text{one left ray} + \text{one right ray}
                         + \text{one two-sided grid}.        \tag{0.6}
\]

The first two rays begin at width `d+2`; the grid begins at width `2d+2`.
The number of relation *types* in (0.6) is constant, but their ordinary
target support need not be.  There are literal two-cut words with identical
stutter collars for which the strict grid contributes

\[
                                   st                       \tag{0.7}
\]

lost targets, and hence quadratically many as the two exterior depths grow.
The correct positive theorem is therefore a compound prepared-deck equality,
not an `O(1)` bank of ordinary targetwise tickets.

## 1. Exact local stutter profile

Write

\[
 E=\{f_2,\ldots,f_{d-1}\},qquad X=Z\cup T.                 \tag{1.1}
\]

For `i>=0`, let

\[
 L_i=\{f_2,\ldots,f_{i+1}\},\qquad
 H_i=\{f_{d-i},\ldots,f_{d-1}\},                           \tag{1.2}
\]

with `L_0=H_0=emptyset`.  Because `K subseteq Z cap T`, the cumulative
boundary unions are

\[
\begin{aligned}
 \operatorname{Suf}_a(Q^-)&=Z\cup L_{(a-2)_+},\\
 \operatorname{Pre}_b(P^+)&=T\cup H_{(b-2)_+},             \tag{1.3}
\end{aligned}
\]

where the indices saturate at `d-2` and the first two values on each shore
coincide.  Consequently the entire local crossing support is

\[
 \boxed{
 \{X\cup L_i\cup H_j:0\le i,j\le d-2\}
  =\{X\cup(E-I):I\text{ empty or a contiguous interval of }E\}.} \tag{1.4}
\]

Thus the stutters change physical multiplicities and deadline alignment,
but not the ungraded local seam support of the unstuttered endpoint wrap.
In particular every new seam target still contains `X`.

### Theorem 1.1 (owner palette)

The values of the length-`d+1` crossing windows are exactly (0.5), in that
order.

#### Proof

The first window contains all of `Q^-` and the initial `T`, so its value is
`U`.  On the next shift, `f_(d-1)` leaves while only the redundant core `K`
enters, giving `D_(d-1)`.  At each subsequent shift the unique absent filler
moves down one index.  The final shift has restored `f_2`, giving `U` again.
\(\square\)

The two copies of `U` are values, not middle owners.  Hence (0.5) is exactly
the palette compatible with two scalar surplus windows; source legality,
simple topology, and common-cap realization are additional requirements.
For (0.5) alone, the weaker assumption `K subseteq C` suffices.  The stronger
assumption (0.2) is needed so that the isolated suffix and prefix rays remain
the literal canonical `A`- and `B`-based coatom flags rather than enlarged
`A union K` and `B union K` flags.

## 2. Exact arbitrary-width exterior ledger

Consider one displayed seam with an arbitrary exterior word `L` before
`Q^-` and `R` after `P^+`:

\[
                         L\;Q^-\mid P^+\;R.                 \tag{2.1}
\]

Let

\[
 S_u=\operatorname{OR}(\operatorname{Suf}_u L),\qquad
 R_v=\operatorname{OR}(\operatorname{Pre}_v R),             \tag{2.2}
\]

and put `S_0=R_0=emptyset`.

### Theorem 2.1 (two rays plus one grid)

Every crossing interval falls into exactly one of the following classes.

1. If it uses at most `d` letters on each shore, its value is a local collar
   value (1.4).
2. If it extends `u>=1` letters beyond `Q^-` on the left and no letters
   beyond `P^+` on the right, its value is

   \[
                              U\cup S_u.                    \tag{2.3}
   \]

3. If it extends `v>=1` letters beyond `P^+` on the right and none beyond
   `Q^-` on the left, its value is

   \[
                              U\cup R_v.                    \tag{2.4}
   \]

4. If it extends on both sides, its value is

   \[
                              U\cup S_u\cup R_v.            \tag{2.5}
   \]

The first uncontrolled crossing width is `d+2`, where (2.3)--(2.4) begin.
The strict grid (2.5) begins at width `2d+2`.

#### Proof

The local case is (1.3).  Once the interval contains all of `Q^-` and at
least the first letter `T` of `P^+`, their union is `U`; further local right
letters add nothing.  This proves (2.3).  The reflected argument proves
(2.4).  If both collars are traversed, the only additional coordinates are
the two exterior cumulative unions, proving (2.5).  The minimum lengths are
immediate.  \(\square\)

Now let `S^-_u,R^-_v` be the exterior chains at the old opened cut and
`S^+_u,R^+_v` those at the newly closed cut.  The exact residual support
condition is

\[
\begin{aligned}
 &\{U\cup S^-_u\}\cup\{U\cup R^-_v\}
        \cup\{U\cup S^-_u\cup R^-_v\}\\
 &\qquad\subseteq
   \mathcal D_{\rm common}
    \cup\{U\cup S^+_u\}\cup\{U\cup R^+_v\}
        \cup\{U\cup S^+_u\cup R^+_v\},                    \tag{2.6}
\end{aligned}
\]

with physical widths retained in every term when deadlines matter.  Exact
occurrence-multiset preservation replaces inclusion by equality.  This is
the full upper-ticket row omitted by the owner-palette calculation.

Two useful sufficient faces are immediate.

* **Pointwise exterior equality:** if the old and new exterior suffix and
  prefix chains agree with the same widths, then every term in (2.6) agrees.
* **Saturation:** if every exterior cumulative union is contained in `U`,
  all three residual families collapse to the single value `U`.

Absent such structure, two one-sided ladder certificates do not certify the
two-sided grid.

There is also a useful nontrivial all-width prepared face.  Form two
macroblocks

\[
                         \mathsf S_i=P^+M_iQ^-              \tag{2.7}
\]

and compare `S_1 S_2` with `S_2 S_1`.  For every
admissible exterior depth `u`, put

\[
\begin{aligned}
 \lambda_i(u)&=U\cup
   \operatorname{OR}(\operatorname{Suf}_u(P^+M_i)),\\
 \rho_i(u)&=U\cup
   \operatorname{OR}(\operatorname{Pre}_u(M_iQ^-)).         \tag{2.8}
\end{aligned}
\]

### Proposition 2.2 (`U`-balanced macroblock equality)

If

\[
                         \lambda_i(u)=\rho_i(u)             \tag{2.9}
\]

for both `i=1,2` and every admissible `u`, then swapping the two macroblocks
preserves the complete length-graded crossing multideck.

#### Proof

The local collar box maps identically.  An old left-only extension in
`S_1` maps, with the same exterior depth and total length, to the new
right-only extension in `S_1`; (2.9) preserves its value.  The
right-only case is symmetric.  An old grid cell with depths `(u,v)` maps to
the new cell `(v,u)`, using (2.9) separately in its two macroblocks.  These
maps are involutions on all crossing occurrences.  \(\square\)

This is a genuine prepared-deck equality theorem, but (2.9) is extra global
structure; the two local stutters do not imply it.

## 3. A literal identical-collar counterexample

The growing residual is compatible with a single cyclic word and two
identical `Q^-|P^+` collars; it is not an artifact of choosing unrelated
interfaces.

Write `D=P^+` and `C_0=Q^-`.  Take fresh singleton tails

\[
 L=(\{\ell_s\},\ldots,\{\ell_1\}),\qquad
 R=(\{r_1\},\ldots,\{r_t\}),                               \tag{3.1}
\]

and two further fresh singleton guards `g,h`.  Define the rotation blocks

\[
\begin{aligned}
 \mathsf P&=D,\{g\},L,C_0,\\
 \mathsf M&=D,R,\{h\},\\
 \mathsf Q&=C_0.                                           \tag{3.2}
\end{aligned}
\]

Then

\[
\begin{aligned}
 W_0&=\mathsf P\mathsf M\mathsf Q
     =D,g,L,C_0\mid D,R,h,C_0,\\
 W_1&=\mathsf M\mathsf Q\mathsf P
     =D,R,h,C_0\mid D,g,L,C_0.                             \tag{3.3}
\end{aligned}
\]

The opened and newly closed cuts both have the literal collar `C_0|D`, and
`W_1` is exactly the required block rotation of `W_0`.  For every

\[
                         1\le u\le s,\qquad1\le v\le t,    \tag{3.4}
\]

the old seam has the target

\[
 G_{u,v}=U\cup\{\ell_1,\ldots,\ell_u\}
                 \cup\{r_1,\ldots,r_v\},                  \tag{3.5}
\]

on an interval of length `2d+u+v`.

### Theorem 3.1 (quadratic ordinary-ticket lower bound)

The `st` targets (3.5) are pairwise distinct and absent from the entire
interval deck of `W_1`.  Hence identical stutter collars can have
targetwise upper debt at least

\[
                                   st.                       \tag{3.6}
\]

#### Proof

Freshness makes the targets distinct.  Any interval in the common block
\(\mathsf P=D,g,L,C_0\) which contains both endpoint fillers \(f_d,f_1\)
must span \(D\) to \(C_0\) and hence contains \(g\), absent from (3.5).
The analogous interval in
\(\mathsf M\mathsf Q=D,R,h,C_0\) contains \(h\).  At the new cut
\(C_0\mid D\), reaching an \(\ell\)-label on the right crosses \(g\), while
reaching an \(r\)-label on the left crosses \(h\).  Thus every possible new
witness has \(g\) or \(h\), whereas (3.5) has neither.  \(\square\)

Restricting to a maximum width `2d+h` and taking both private blocks long
enough leaves all pairs `u,v>=1` with `u+v<=h`; this already gives

\[
                              \frac{h(h-1)}2.                \tag{3.7}
\]

strict grid targets.  Hence the arbitrary-width residual grows
quadratically in the exterior depth even though the complete lower/owner
band is exact.

Moreover, inclusion among (3.5) is exactly the product order on
\([s]\times[t]\).  For \(s=t=d\), the diagonal \(u+v=d+1\) is an antichain
of size \(d\), and fixing \(u\) gives a \(d\)-chain cover.  The residual
poset therefore has width exactly \(d\): it cannot be represented by
\(O(1)\) nested rays either.

## 4. Consequence for `B+2`

The audited implication is now precise.

* `B+1` endpoint wrapping is flat-owner impossible on the prepared dropped
  bank.
* `B+2` with two core stutters fixes that exact owner-palette obstruction
  and, conditional on planting identical collars, preserves every crossing
  row through width `d+1`.
* It does not turn the full upper interface into `O(1)` ordinary rays.  The
  exact residual is two rays plus one compound grid, and the grid can carry
  quadratically many last-witness targets.

Thus a `B+2` theorem still needs one of:

1. a pointwise/graded exterior-deck equality as in (2.6);
2. unaffected duplicate witnesses for the residual rays and grid;
3. a literal compound-grid absorber which repays all its cells jointly; or
4. direct construction of the rotated chronology before final upper-owner
   and common-cap assignment.

The stutter bank is a correct short-band boundary primitive, not yet an
arbitrary-width universal-word recursion.

The phrase `B+2` is itself local until the host is built: addresswise
cancellation uses distinct physical copies of `Q^-|P^+` at the old and new
cuts.  The two inserted `K` values do not by themselves plant all required
collar copies in one Pascal child.

## 5. Audit

The independent replay

```text
python3 scratch/audit_k_bplus2_stutter_full_upper_ledger_20260801.py
```

checks the owner list and full local seam support for `2<=d<=40`, 1,694
arbitrary-exterior cells, and 324 guarded two-cut counterexamples.  It
reports

```text
PASS_K_BPLUS2_STUTTER_FULL_UPPER_LEDGER
```

with canonical payload SHA-256

```text
49d8019a0b972a490bf67ef53ae7ee3072d227d05a143a1854c00e5a5d496f7d
```

and frozen summary

```text
scratch/k_bplus2_stutter_full_upper_ledger_20260801.audit.json
```
