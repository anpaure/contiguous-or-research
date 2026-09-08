# Audit of the fractional factorable-braid packing and integral reduction

## Scope and verdict

This note audits Sections 2--3 of the proposed long-run-atom argument: the
definition of the symmetric-chain quotas, the permutation-orbit fractional
weighting, the initialization estimate, the integer quotas, the alteration
scale, the rank-defect estimates, the outer tail, and the odd-dimensional
lift.

The verdict is:

* **Theorem 1: PASS, conditional on the previously proved long-run MTF atom
  lemma.**  The normalization is correct and the total initialization cost is
  `o(W)`.
* **Theorem 2: PASS as a sufficient conditional reduction.**  If the stated
  conflict-free typed packing exists with the stated quota accuracy, then its
  traversal followed by literal insertion has length `(1+o(1))W`.
* The argument does **not** prove that the required integral packing exists.
  Therefore it does not prove the constant-one theorem.

Three formal clarifications are required.  The orbit should be an orbit of
**labelled atoms** (parallel centre edges must not be collapsed); the phrase
"apart from alterations" should be replaced by an explicit `l1` bound on the
type-count vector; and

\[
H=\left\lfloor m-3\log _2m-h\right\rfloor
\]

should be used to make the common atom length integral.

## 1. The telescoping quota ledger

Let

\[
N_q=\binom{2m}{m-q},\qquad
c_d=N_d-N_{d+1}\quad(0\le d<h),\qquad c_h=N_h.
\]

Then, exactly,

\[
\sum_{d=q}^h c_d
=\sum_{d=q}^{h-1}(N_d-N_{d+1})+N_h=N_q,
\]

and in particular `sum c_d=N_0=W`.  All `c_d` are nonnegative integers.
This is the correct truncated symmetric-chain ledger: `c_h` aggregates every
chain whose full radius is at least `h`.

## 2. Orbit normalization

For a fixed type `d`, let `A_d` be the labelled orbit of one radius-`d`,
length-`H` atom under the full coordinate-permutation group.  Give the orbit
total mass `c_d/H`, equivalently give each labelled orbit element weight

\[
\frac{c_d}{H|\mathcal A_d|}.
\]

Every atom contains `H` distinct masks in each rank `m-q` and `m+q` for
`q<=d`.  Coordinate transitivity implies that a fixed mask at depth `q` is
contained in

\[
\frac{|\mathcal A_d|H}{N_q}
\]

labelled atoms.  Its load from type `d` is consequently `c_d/N_q`, and its
total load is

\[
\frac1{N_q}\sum_{d=q}^h c_d=1.
\]

At `q=0` this is the claimed unit centre load.  The total atom mass is

\[
\sum_{d=0}^h\frac{c_d}{H}=\frac WH.
\]

Stabilizers cause no normalization problem, provided the orbit is treated as
a group-invariant labelled atom system.  Defining an edge only by its set of
middle centres can collapse atoms with different exposed strips and makes the
conflict relation ambiguous; the integral object should therefore be a
labelled multi-hypergraph.

## 3. Initialization and portal cost

A radius-`d` atom with `H` states has word length at most

\[
(2d+2)+(H-1)=H+2d+1.
\]

Thus its excess is at most `2d+1`.  The fractional total excess is

\[
\frac1H\sum_{d=0}^h c_d(2d+1)
\le \frac{(2h+1)W}{H}.
\]

For

\[
h=\lceil\sqrt{m\log m}\rceil,
\qquad H=\lfloor m-3\log _2m-h\rfloor,
\]

we have `h/H=O(sqrt(log(m)/m))=o(1)`, so this is `o(W)`.  This verifies the
claimed global amortization.  It is conditional only on the existence and
initialization bound of the long-run atoms.

## 4. Exact integer quotas and quota alterations

Put

\[
b_d=\left\lfloor\frac{c_d}{H}\right\rfloor.
\]

For the exact quota vector,

\[
0\le W-H\sum_{d=0}^h b_d<H(h+1).
\]

To formalize the proposed alteration allowance, let `a_d` be the actual
number of selected atoms of type `d` and require

\[
\eta:=\sum_{d=0}^h|a_d-b_d|
=o\left(\frac{W}{Hh}\right).
\]

If the selected labelled atoms have disjoint centre edges, their number `C`
of exposed middle masks satisfies

\[
C=H\sum_da_d\le W
\]

and

\[
0\le W-C<H(h+1)+H\eta
=O(Hh)+o(W/h).
\]

This is the precise form of equation (16).

The reset excess is bounded by

\[
\begin{aligned}
R
&\le \sum_d b_d(2d+1)+(2h+1)\eta\\
&\le \frac{(2h+1)W}{H}+(2h+1)\eta=o(W).
\end{aligned}
\]

This verifies equation (17), including the effect of alterations.

## 5. Rank defects

Conflict-freeness makes all designated strip masks at a fixed noncentral rank
distinct.  At depth `q`, the exposed count is

\[
E_q=H\sum_{d=q}^h a_d\le N_q.
\]

Using the telescoping identity and the floor errors,

\[
0\le N_q-E_q
<H(h-q+1)+H\eta
=H(h-q+1)+o(W/h).
\]

This is equation (18), with the alteration term made explicit.  The total
number of missing masks in the complete central band is at most

\[
(N_0-E_0)+2\sum_{q=1}^h(N_q-E_q)
=O(Hh^2)+O(Hh\eta)=O(Hh^2)+o(W).
\]

Since `H=Theta(m)` and `h^2=Theta(m log m)`, the first term is
`O(m^2 log m)=o(W)`.  This verifies equation (19).  Counting `q=0` twice, as
the informal prose can be read to do, is harmless as an upper bound, but the
display above is the exact rank accounting.

## 6. Literal completion and the outer tail

Concatenating the genuine atom words preserves every internal witness.
Appending every missing nonempty mask literally represents it by a singleton.
No compatibility condition is needed between different concatenated atoms.

For `X~Bin(2m,1/2)`, Hoeffding's inequality gives

\[
\sum_{r=0}^{m-h-1}\binom{2m}{r}
\le 4^m\exp\left(-\frac{(h+1)^2}{m}\right)
=O(4^m/m)
\]

when `log` in the definition of `h` is the natural logarithm (another fixed
base only changes the polynomial power).  The upper tail has the same size.
Because

\[
W=\binom{2m}{m}=\Theta(4^m/\sqrt m),
\]

both outer tails together contain `o(W)` masks.  The empty mask included in
the displayed binomial sum should simply not be appended in the zero-free
problem; its inclusion only enlarges the upper bound by one.

Combining traversal length, reset excess, central-band defects, and tails
therefore gives

\[
\nu(2m)\le W+o(W).
\]

This conclusion is conditional on the typed conflict-free matching.

## 7. Odd-dimensional lift

The established trimmed lift gives

\[
\nu(2m+1)\le2\nu(2m).
\]

The exact width relation is

\[
W(2m+1)=\binom{2m+1}{m}
=\frac{2m+1}{m+1}W(2m),
\]

so

\[
\frac{2W(2m)}{W(2m+1)}
=\frac{2m+2}{2m+1}=1+O(1/m).
\]

Thus the even-dimensional conditional conclusion propagates correctly to odd
dimensions.  The reciprocal ratio appearing elsewhere,
`W(2m+1)/(2W(2m))=(2m+1)/(2m+2)`, is equivalent.

## 8. Scope correction

The phrase "the only obstruction" is justified only **within this long-run
atom route**.  The calculation proves that, once the atom lemma is imported,
portal/reset cost, factorability, and tails are not asymptotic bookkeeping
obstructions.  It does not establish that the conflict-free matching exists,
nor that no different global obstruction can prevent this particular atom
architecture from being rounded.  The mathematical frontier is accurately
stated as the following conditional target:

> Find a conflict-free matching in the labelled atom multi-hypergraph with
> type counts `a_d` satisfying
> `sum_d |a_d-floor(c_d/H)|=o(W/(Hh))`.

That target is sufficient for the constant-one upper bound, but remains
unproved.
