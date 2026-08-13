# Period-`q+2` schedules program complete nested tickets

**Date:** 2026-08-13  
**Status:** exact local theorem and exact global reduction.  Every strict
nested lower ticket ending at a prescribed immediate-lower root has a
literal portal into an upper-rich period-`q+2` distributed-core packet.
This is stronger than one-cell programmability.  It does not choose
pairwise owner-disjoint portals for all tickets; that coupled packet design
remains the global gate.

## 1. Setup

Let the owner rank be `R`, let `q>=4`, and assume

\[
                         R\geq q,\qquad k-R+1\geq3.         \tag{1.1}
\]

Put

\[
                         N=q+2.                              \tag{1.2}
\]

All phase indices below lie in `Z_N`.  For `a in Z_N`, use the two-emission
schedule

\[
                         P_a=\{a,a+q-1\}=\{a,a-3\}.          \tag{1.3}
\]

The two cyclic gaps of `P_a` are `q-1` and `3`.  Consequently every cyclic
interval of `q-1` phases meets `P_a`.

Fix a rank-`R-1` set `Q` and a strict chain

\[
 \varnothing=V_0\subsetneq V_1\subsetneq\cdots\subsetneq
 V_{q-1}=Q.                                                 \tag{1.4}
\]

The members need not have consecutive ranks.

## 2. A rotation is an exact suffix threshold

Use phase `0` as the right endpoint, and write

\[
                         J_\ell=\{-\ell+1,\ldots,0\},
             \qquad 1\leq\ell\leq q-1.                    \tag{2.1}
\]

### Lemma 2.1 (all threshold words occur)

For every `1<=t<=q-1`, put

\[
                         a_t=-t+1\pmod N.                    \tag{2.2}
\]

Then

\[
                         P_{a_t}\cap J_\ell\ne\varnothing
                  \quad\Longleftrightarrow\quad \ell\geq t.
                                                                    \tag{2.3}
\]

#### Proof

In the integer representatives `-(q+1),...,0`, the two emissions are

\[
                         -t+1\quad\hbox{and}\quad -t-2.     \tag{2.4}
\]

The second is three positions farther to the left.  If `ell<t`, the left
endpoint `-ell+1` of `J_ell` lies strictly to the right of both emissions.
If `ell>=t`, the first emission `-t+1` belongs to `J_ell`.  The endpoint
case `t=q-1` gives the second emission `-q-1`, still outside every
`J_ell` under consideration.  This proves (2.3).  \(\square\)

## 3. Complete-ticket programmability

For every `1<=ell<=q-1`, choose

\[
                         y_\ell\in V_\ell-V_{\ell-1}.       \tag{3.1}
\]

These labels are distinct.  Put

\[
                         Y=\{y_1,\ldots,y_{q-1}\},
                         F=Q-Y.                              \tag{3.2}
\]

Thus `|F|=R-q`.  Choose three further distinct labels

\[
                         y_q,y_{q+1},y_{q+2}\notin Q,       \tag{3.3}
\]

and cyclically order the `N` toggle labels so that phase `-ell+1` carries
`y_ell` for `1<=ell<=q-1`, while the remaining three phases carry
`y_q,y_(q+1),y_(q+2)` in any fixed order.

For `f in F`, define its threshold

\[
                         t(f)=\min\{\ell:f\in V_\ell\},     \tag{3.4}
\]

and assign it the schedule `P_(a_(t(f)))`.  If `G_i` denotes the core
coordinates emitting at phase `i`, use the source letter

\[
                         A_i=G_i\cup\{y(i)\},               \tag{3.5}
\]

where `y(i)` is the toggle at phase `i`.

### Theorem 3.1 (arbitrary complete nested ticket)

The source ring (3.5) is an upper-rich period-`q+2` pure rail and its
suffixes ending at phase `0` satisfy

\[
                         \bigcup_{i\in J_\ell}A_i=V_\ell
                 \qquad(1\leq\ell\leq q-1).               \tag{3.6}

Every interval of width at least `q-1` has exactly the same union as in the
repeated-core two-hole ring.  Hence the decoration preserves literally the
complete immediate-lower, owner, and immediate-upper rows, including the
owner Johnson cycle and their simplicity.

#### Proof

By construction, the toggle labels in `J_ell` are exactly

\[
                         \{y_1,\ldots,y_\ell\}.             \tag{3.7}
\]

For `f in F`, Lemma 2.1 says that some emission of `f` lies in `J_ell`
exactly when `t(f)<=ell`, which is equivalent to `f in V_ell`.  Therefore
the core contribution to the suffix union is `F cap V_ell`.  Strictness of
(1.3) and (3.1) also give

\[
 V_\ell\cap Y=\{y_1,\ldots,y_\ell\}.                       \tag{3.8}
\]

Equations (3.7)--(3.8) prove (3.6).

Every schedule `P_a` meets every cyclic `(q-1)`-interval.  Thus all core
coordinates occur in every interval of width at least `q-1`; the toggle
part is unchanged.  Those rows are consequently identical to the
repeated-core ring.  At widths `q-1,q,q+1` they have ranks `R-1,R,R+1`
and are the standard simple two-hole lower, owner, and upper rows.
\(\square\)

### Corollary 3.2 (partial tickets and marked rank jumps)

Any nonempty chain of at most `q-1` subsets ending at `Q` can be embedded
as marked members of such a suffix ticket.  Indeed, extend it inside `Q`
to a strict chain of length `q-1`, apply Theorem 3.1, and mark only the
original members.  Arbitrary positive rank jumps are allowed.

### Proposition 3.3 (exact multi-endpoint age normal form)

Fix one frame: a core `F` and a cyclic toggle order `(y_t)_(t in Z_N)`.
For a schedule `E subseteq Z_N` meeting every `(q-1)`-interval, define

\[
 \alpha_t(E)=1+\min\{s\geq0:t-s\in E\}.                     \tag{3.9}
\]

Then `1<=alpha_t(E)<=q-1`, and

\[
 \alpha_t(E)=
 \begin{cases}
  1,&t\in E,\\
  \alpha_{t-1}(E)+1,&t\notin E.
 \end{cases}                                               \tag{3.10}
\]

Conversely, every cyclic integer word in `[q-1]` satisfying (3.10), with
`E={t:alpha_t=1}`, is the age word of a unique such emission set.

Consequently a family of `N` complete endpoint tickets belongs to one
distributed-core packet exactly when, after removing the fixed toggle
suffix

\[
                         I_{t,\ell}=\{y_{t-\ell+1},\ldots,y_t\},          \tag{3.11}
\]

every core coordinate `f` has membership

\[
 f\in V_{t,\ell}
       \quad\Longleftrightarrow\quad \ell\geq\alpha_t(f)    \tag{3.12}
\]

for one cyclic age word satisfying (3.10).  If only the two-emission
schedules `P_a` are allowed, each age word is a rotation of

\[
                         (1,2,\ldots,q-1,1,2,3).            \tag{3.13}
\]

#### Proof

Equation (3.9) is the backward distance to the latest emission, plus one.
Moving the endpoint forward either meets a new emission and resets the age
to one, or increases that distance by one.  The hitting condition is
equivalent to the age never exceeding `q-1`, proving (3.10).  Conversely,
(3.10) reconstructs the last reset at every phase, so `E` is unique.

A core coordinate occurs in an `ell`-suffix precisely when its latest
emission has backward distance at most `ell-1`; this is (3.12).  The toggle
contribution is (3.11).  Finally `P_a` has cyclic gaps `q-1` and `3`, so
the ages ramp from one through the length of each gap, giving (3.13).
\(\square\)

Proposition 3.3 is the exact compatibility omitted by a one-ticket portal:
at different endpoints the thresholds are not free variables but one
capped countdown word per core coordinate.

## 4. Exact portal count and the coupling that remains

For a fixed chain (1.3), construction (3.1) has

\[
                         \prod_{\ell=1}^{q-1}
                         |V_\ell-V_{\ell-1}|              \tag{4.1}

choices for its distinguished toggle labels.  After those are fixed, the
three exterior toggle labels have

\[
                         (k-R+1)_3                         \tag{4.2}

ordered choices.  Thus even a saturated chain, whose increments are all
singletons, has a polynomially large labelled portal bank.  Additional
cyclic reversal and endpoint choices may enlarge it.

These portals cannot be selected independently.  Two choices may share an
owner, an immediate-lower root away from the distinguished endpoint, an
upper colour, or a physical packet.  More importantly, one physical packet
has `N` endpoint tickets but only one schedule for each core coordinate.
The threshold words at its different endpoints must therefore be cyclic
translates of one common emission word.  Selecting `N` unrelated
one-endpoint portals and declaring them to be one packet is invalid; it
would overcount the owner resource by a factor `N`.

The exact global object is therefore a grouping of complete-ticket portals
into schedule-compatible `N`-tuples, followed by a rainbow packet selection
which simultaneously:

1. uses every rank-`R` owner once;
2. uses every rank-`R-1` root once;
3. assigns a provider to every rank-`R+1` target; and
4. uses every required lower chain once.

The theorem proves that no individual nested ticket or source schedule is
an obstruction.  It does not prove the multi-endpoint compatibility or this
joint selection.

## 5. Reduction to the punctured-half equitable-chain gate

Let `L` be all nonempty targets below rank `R`, and let a Ferrers boundary
remove named families `B_s`.  A partition of the residual family into `W`
chains of size at most `q-1`, one ending at each rank-`R-1` root, supplies
exactly the ticket input to Corollary 3.2.  Conversely, if a depth-`q`
chronology is equipped with selected suffix marks which cover every
residual target exactly once, then its marked endpoint tickets give such a
chain family after the terminal boundary occurrences are removed.  No
assertion is made for an arbitrary unmarked chronology.

Thus the static target row is precisely the Ferrers-profiled equitable
half-chain problem recorded in
`MATH_THEOREM_FERRERS_PUNCTURED_HALF_LATTICE_EQUAL_CHAIN_EQUIVALENCE_20260807.md`.
The new content here is that every member of a solution to that static
chain problem has a local upper-rich source portal with all three top shores
unchanged.  To lift the whole chain partition, its members must still be
grouped into schedule-compatible endpoint tuples.  Thus the surviving
difficulty is the common integral portal/owner chronology, not an
individual-ticket obstruction.

## 6. Scope

The construction is local to a closed packet.  It does not prove an exact
packet factor, an equitable half-chain decomposition, component fusion, or
the final linear cap.  Opening packets can create exterior intervals, which
require a separate seam ledger.
