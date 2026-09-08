# Audit: balanced overload and the decorated-wreath reduction

## Verdict

The balanced-overload formulas are useful and mostly correct, but three
substantive corrections are required.

1. Exact middle wreath factors for `(n,k)=(2m+1,m)` are already known.  The
   opening claim that this central case of the wreath conjecture remains open
   is false.
2. The proof of collision domination must choose balancing transfers
   carefully; an arbitrary pair with load gap at least two need not lower the
   minimum balanced `L1/2` distance.
3. The nonzero clone-defect equivalence is false with only core and one bonus
   clone.  Loads larger than `c_q+1` cannot be decorated.  Adding unpenalized
   spill slots repairs the equivalence exactly.

After these corrections, MWB is a valid open sufficient condition, but it is
strictly stronger than the existing factorial-energy hole gate and is not the
weakest known missing theorem for coefficient one.

## 1. Exact central wreath factors exist

Mütze, Standke, and Wiechert prove that the odd graph `O_(2m+1)` has a
`C_(2m+1)`-factor for every `m` (Theorem 4 of arXiv:1603.02525).

Every cycle of that minimum odd length is a wreath.  For a cycle
`A_0,...,A_(2m)`, label edge `A_i A_(i+1)` by the unique coordinate

\[
 z_i=[2m+1]\setminus(A_i\cup A_{i+1}).
\]

If one coordinate never occurred as a label, its membership would toggle on
all `2m+1` cycle edges and could not return to its initial value.  Thus the
`2m+1` labels are all coordinates exactly once, and iteration gives

\[
 A_i=\{z_{i+1},z_{i+3},\ldots,z_{i+2m-1}\}.
\]

After multiplying indices by two modulo `2m+1`, these are the ordinary
length-`m` cyclic intervals of one coordinate order.  Hence an exact middle
wreath factor is unconditional.

The Petr--Turek conjecture cited in the submitted statement is the general
wreath conjecture; their stronger Dyck-labelled central variants remain
conjectural.  It does not undo the known undecorated central factor.

MWB remains open because no known central factor has the required common
multidepth balancing, not because middle ownership itself is missing.

## 2. Exact overload formula

Let `T=cN+r`, `0<=r<N`, and let integer loads `x_S` have total `T`.  Put

\[
 a_t=|\{S:x_S\ge t\}|.
\]

The submitted identities are correct:

\[
 O=\sum_{t=1}^{c}(N-a_t)+(r-a_{c+1})_+
 =\sum_S(c-x_S)_+ +(r-a_{c+1})_+,
\]

and

\[
 O=\frac12\min_b\sum_S|x_S-b(S)|,
\]

where `b` ranges over the balanced quota vectors with `r` entries `c+1`
and all others `c`.

The first term counts uncovered units in the `c` core layers.  Raising `r`
quotas removes one overload unit at at most `min(r,a_(c+1))` targets, giving
the bonus-shortage term exactly.

## 3. Collision domination, with a corrected proof

Let

\[
 P=\sum_S{x_S\choose2},\qquad
 P^{\min}=N{c\choose2}+rc,
\]

and put `d_S=x_S-c`.  Since `sum d_S=r`, exact algebra gives

\[
 Q:=P-P^{\min}=\frac12\sum_Sd_S(d_S-1).
\]

Define

\[
 D^- =\sum_S(-d_S)_+,
 \qquad
 D^+ =\sum_S(d_S-1)_+.
\]

The identity `sum d_S=r` implies

\[
 D^+-D^-=r-a_{c+1},
 \qquad
 O=\max\{D^-,D^+\}.
\]

Pointwise,

\[
 \frac12d(d-1)\ge
 \begin{cases}
 -d,&d\le0,\\
 0,&d=1,\\
 d-1,&d\ge2.
 \end{cases}
\]

Therefore

\[
 Q\ge D^-+D^+\ge O.
\]

This proves the submitted inequality.  Its proposed move proof is not valid
for an arbitrary gap-two pair.  For example, with `c=2,r=2` and loads
`(5,3,0)`, moving one unit from 5 to 3 gives `(4,4,0)` while `O` stays 2.
One may instead choose an extremal donor/receiver or use the direct proof
above.

## 4. Orbit quota averaging

Conditional on any one exact factor `F`, its `n!` coordinate relabelings
satisfy

\[
 \sum_\sigma\mu_q^{\sigma F}(S)=\frac{n!W}{N_q}.
\]

Since `N_q` divides `n!`, a biregular bipartite incidence assignment gives
every factor copy exactly `r_q` upper quotas and every target exactly
`n!r_q/N_q` such quotas.  This may be done independently at every depth.

This proves absence of a rankwise aggregate row-sum divisibility obstruction.
It does **not** rule out per-copy point-margin constraints, cross-depth
compatibility, support restrictions, or integral trade-lattice obstructions.
The broader “no lattice obstruction” wording is therefore unjustified.

## 5. Zero overload and the missing spill slots

The core-plus-one-bonus decorated hypergraph correctly characterizes exact
zero overload: a middle-perfect matching covering all core clones exists iff
every load is `c_q` or `c_q+1`.

It does not represent a general factor with finite positive overload.  If
`mu_q(S)>c_q+1`, there are more occurrences than available clones for `S`, so
no decoration is possible.  The abstract load vector `(0,0,3)` with
`N=3,c=1,r=0` is the smallest illustration: `O=2`, but three occurrences at
the heavy target cannot use only its core and bonus clones.

### Exact spill-augmented correction

Let `B=W/(2m+1)` be the number of wreaths in a factor.  For every `(q,S)`,
provide `B` distinct slots:

- the first `c_q` are penalized core slots;
- the next slot, when `c_q<B`, is the bonus slot;
- all remaining slots are unpenalized spill slots.

This is enough because a target occurs at most once in one wreath, so its
factor load is at most `B`.

For a middle-perfect decorated matching `M`, define

\[
 \delta_q(M)=
 \#\{\text{uncovered core slots}\}
 +\bigl(r_q-\#\{\text{covered bonus slots}\}\bigr)_+.
\]

For a fixed factor `F`, assigning the first `mu_q(S)` slots at every target
gives

\[
 \delta_q=\sum_S(c_q-\mu_q(S))_+
 +(r_q-a_{q,c_q+1})_+=O_q(F).
\]

Conversely, using a bonus or spill while leaving a usable core vacant cannot
decrease `delta_q`: replacing a core use by a bonus raises the core deficit by
one and lowers the bonus shortage by at most one.  Spill use cannot improve
the objective.  Thus

\[
 \min_{M\text{ decorating }F}\delta_q(M)=O_q(F).
\]

Depth decorations are independent, so the corrected exact statement is

\[
 \min_{M\text{ decorating }F}
 \sum_{q\le H}\frac{\delta_q(M)}{c_q}
 =\sum_{q\le H}\frac{O_q(F)}{c_q}.
\]

MWB is therefore equivalent to a **spill-augmented** weighted clone-defect
problem, not the submitted core-plus-bonus matching problem.

## 6. Comparison with the weaker coefficient-one gate

The Catalan-scale implication

\[
 O_q=O(c_q\operatorname{Cat}_m)
 \quad\Longrightarrow\quad
 \sum_{q\le H}\frac{O_q}{c_q}=o(W)
\]

is valid when `H=o(m)`.

However MWB is stronger than needed for the current OR transfer.  With

\[
 Q_q=P_q-P_q^{\min}=\Delta_{q,2},
\]

the submitted collision route asks for

\[
 \sum_q\frac{Q_q}{c_q}=o(W).
\]

The existing factorial-energy hole theorem only requires

\[
 \sum_q\frac{Q_q}{{c_q+1\choose2}}=o(W),
\]

and can use the still weaker rankwise hybrid minimum

\[
 \sum_q\min\left\{
 \frac{O_q}{c_q},
 \frac{Q_q}{{c_q+1\choose2}}
 \right\}=o(W).
\]

Accordingly the uniform bound

\[
 Q_q=O\!\left({c_q+1\choose2}\operatorname{Cat}_m\right)
 =O(c_q^2\operatorname{Cat}_m)
\]

already suffices for the hole-transfer lane, whereas MWB via collision asks
for the stronger `O(c_q Cat_m)` estimate.

Thus MWB is a legitimate open integral balancing target, but it is neither
blocked by existence of exact central factors nor the weakest known theorem
whose proof would yield coefficient one.
