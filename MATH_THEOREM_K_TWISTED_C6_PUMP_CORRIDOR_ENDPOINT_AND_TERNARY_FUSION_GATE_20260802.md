# Twisted `C6` pump: exact corridor endpoint state and the ternary fusion gate

**Date:** 2026-08-02  
**Lane:** K, ambient use of the phase-split unit pump  
**Status:** exact endpoint-history/voltage calculus, a sharp two-edge
lower-palette obstruction, and a sufficient three-edge fusion interface.
Existence of the required protected owner/`q1` host and of a prepared
history-compatible Boolean hex is not asserted.

## 0. Verdict

Let `k=2r-1`, let the history depth be `d`, and put `h=d+1`.  The twisted
three-run pump exists when

\[
                         r\ge 3d+4.                    \tag{0.1}
\]

Its chosen branch is one physical cycle of voltage `epsilon in {+1,-1}`
with a literal private closing edge.  The opened fixed-`z` seven-ear packet
has zero **relative** two-phase displacement.  These facts compose exactly:
if both packets are embedded in one occurrence-labelled host, are disjoint,
and every later seven-ear ticket has zero completed displacement, the
seven-ear changes do not alter `epsilon`.

There are nevertheless two independent ambient gates.

1.  The present small protected-factor theorem cannot plant the developed
    pump.  The pump contains `3k` Johnson edges, hence `6k` middle-levels
    incidence edges, whereas that theorem allows only `r-2` protected
    incidence edges.  In fact

    \[
                         6k=12r-6>r-2.                 \tag{0.2}
    \]

    Thus a quotient-equivariant or prospective owner/`q1` completion is a
    genuine extra theorem, not a consequence of the bounded-collar result.

2.  A post-hoc two-edge splice of the pump into an exact lower-`q1` factor
    cannot be palette-transparent.  The first possible transparent repair
    is a three-edge Boolean hex.  Use a pump edge different from the private
    closure as one old hex edge, and two prepared old host edges as the
    other two.  If the three old edges lie on distinct components, the hex
    merges them to one component, preserves all four central resource
    palettes, and leaves the private pump edge untouched.  It preserves the
    unit voltage exactly when its occurrence-labelled signed charge is zero.

The history condition for that correction is not heuristic.  It is the
conjunction of three explicit positive and three explicit negative collar
tests in Theorem 4.1 below.

## 1. Literal boundary state of the twisted pump

Use the notation of
`MATH_THEOREM_K_TWISTED_THREE_RUN_C6_DYADIC_PUMP_AND_HISTORY_APERTURE_20260802.md`.
Let `N=3k` and enumerate the forward cycle edges by `j=0,...,N-1`.  Write

\[
 \alpha_j=p_{j\bmod3}+\lfloor j/3\rfloor,\qquad
 \beta_j=q_{j\bmod3}+\lfloor j/3\rfloor
                    \pmod k,                            \tag{1.1}
\]

so edge `j` deletes `alpha_j` and inserts `beta_j`.  Cut edge `N-1`.
The forward open pump path `P` uses events `0,...,N-2`.  Its exact positive
collars are

\[
\begin{aligned}
 D^+(P)&=(\alpha_0,\ldots,\alpha_{d-1}),\\
 I^+(P)&=(\beta_{N-2},\beta_{N-3},\ldots,\beta_{N-d-1}),
\end{aligned}                                           \tag{1.2}
\]

and its negative, zero-run collars are

\[
\begin{aligned}
 D^-(P)&=(\beta_0,\ldots,\beta_{d-1}),\\
 I^-(P)&=(\alpha_{N-2},\alpha_{N-3},\ldots,\alpha_{N-d-1}).
\end{aligned}                                           \tag{1.3}
\]

For a cut at a general edge `c`, rotate every index in (1.2)--(1.3) by
`c+1` modulo `N`.  Reversing the pump exchanges `D` and `I` in each
polarity and negates the voltage.

### Lemma 1.1 (the collars are the complete endpoint state)

For a pump cut and an exterior path of at least `d` transitions, the four
tuples (1.2)--(1.3), together with the two connector labels, are necessary
and sufficient for all positive and negative runs crossing the two joins.

#### Proof

For positive residence, the directed-history automaton remembers the last
`d` insertion labels; hence its first-deletion and last-insertion collars
are exactly (1.2).  For negative residence exchange deletion and insertion,
giving (1.3).  The explicit collar recurrence checks every cross-boundary
insertion/deletion pair whose separation is at most `d`; all other runs are
internal to one path.  \(\square\)

This is the endpoint state which must be admitted by the ambient ticket.
The scalar statement “the pump is resident” does not replace it.

## 2. Exact serial insertion equations

Let a resident host cycle contain a directed edge

\[
                            f:x\longrightarrow y.
\]

Deleting `f` leaves a directed path `H:y leadsto x`.  Let the selected pump
branch have open path `P:q leadsto p` and private closure

\[
                            e_*:p\longrightarrow q.
\]

Suppose the two crossed seams

\[
                   a:x\longrightarrow q,\qquad
                   b:p\longrightarrow y                \tag{2.1}
\]

are literal Johnson edges.  For a polarity `nu in {+,-}`, define
`G_d^nu(A,e,B)` to be the exact connector test

\[
\begin{aligned}
 \operatorname{del}_\nu(e)&\notin I^\nu(A),\\
 \operatorname{ins}_\nu(e)&\notin D^\nu(B),\\
 I_i^\nu(A)&\ne D_j^\nu(B)\quad(i+j\le d),              \tag{2.2}
\end{aligned}
\]

where `(del_+,ins_+)=(del,ins)` and
`(del_-,ins_-)=(ins,del)`.

### Theorem 2.1 (exact two-seam endpoint and voltage test)

The crossed chronology

\[
                             H\,a\,P\,b                 \tag{2.3}
\]

is biresident at every new boundary if and only if

\[
 G_d^\nu(H,a,P)\quad\hbox{and}\quad G_d^\nu(P,b,H)
       \qquad(\nu=+,-).                                 \tag{2.4}
\]

Its voltage relative to the disjoint host and pump cycles changes by

\[
 \chi(a,b;f,e_*)=
 \delta(a)+\delta(b)-\delta(f)-\delta(e_*).             \tag{2.5}
\]

Consequently, if `chi=0`, the merged chronology has voltage

\[
                       v_{\rm host}+\epsilon.           \tag{2.6}
\]

The selected pump is the unique absolute-voltage actuator only when the
nonpump host contribution is the declared zero-holonomy value.  Zero
**relative** displacement of the two seven-ear phases proves that both
phases have the same value in (2.6); it does not by itself prove that
`v_host=0`.

#### Proof

Equation (2.4) is the collar recurrence at the only two changed joins.
All unchanged internal runs stay valid.  Additivity of the lifted edge
labels gives (2.5).  The completed pump total is `epsilon`, so zero switch
charge gives (2.6).  \(\square\)

For an exact resource table, (2.4)--(2.5) must be supplemented by

\[
 \mathcal R(a)\mathbin{\dot\cup}\mathcal R(b)
 =\mathcal R(f)\mathbin{\dot\cup}\mathcal R(e_*),       \tag{2.7}
\]

or by explicit backup rows.  In particular its lower and immediate-upper
projections are

\[
 \{I(a),I(b)\}=\{I(f),I(e_*)\},\qquad
 \{U(a),U(b)\}=\{U(f),U(e_*)\}.                        \tag{2.8}
\]

## 3. Sharp obstruction to a transparent two-edge fusion

### Theorem 3.1 (lower-`q1` two-edge no-go)

Let `xy,pq,xq,py` be four Johnson edges on four distinct rank-`r`
owners.  If

\[
 \{x\cap y,p\cap q\}=\{x\cap q,p\cap y\},             \tag{3.1}
\]

then `x cap y=p cap q`.  Hence a nondegenerate crossed two-edge splice
cannot preserve an exact lower-`q1` palette whose old colours are distinct.

#### Proof

There are two possible pairings in (3.1).  If
`x cap q=x cap y=L`, then `y` and `q` both contain the same
rank-`(r-1)` subset `L` of `x`.  The other equality says that `y` and `q`
also contain the same rank-`(r-1)` subset `M` of `p`.  Since distinct
rank-`r` sets `y,q` have intersection of rank `r-1`, both `L` and `M`
equal `y cap q`; hence `L=M` and the two old colours agree.

In the crossed pairing, `x cap q=p cap q=M` and
`p cap y=x cap y=L`.  Thus both `x` and `p` contain `L union M`.
If `L!=M`, that union has rank `r`, forcing `x=p`, contrary to the four
distinct endpoints.  Therefore again `L=M`.  \(\square\)

The common-facet clique is the equality case, but it already repeats one
lower colour.  Thus (2.7) is impossible on the exact lower-rainbow face.
This is the smallest literal incompatibility in a universal post-hoc pump
planting theorem.  A cap or history marginal cannot repair it.

## 4. Corrected three-edge Boolean-hex fusion

Use the literal Boolean hex notation

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\}.                           \tag{4.1}
\]

Take `E->F` to be a pump edge **different from** `e_*`.  Delete the three
old edges.  Let

\[
 P_1:B\leadsto A,\qquad P_2:D\leadsto C,\qquad
 P_3:F\leadsto E                                      \tag{4.2}
\]

be the resulting directed paths; `P_3` contains the untouched private
edge `e_*`.

### Theorem 4.1 (history-correct transparent fusion)

Assume the three old edges lie on three distinct directed cycles and the
six typed hex atoms are literal occurrence-labelled resources.  Replacing
`O` by `N` gives one directed cycle and preserves the complete owner,
lower, immediate-upper, tail, and head inventories.  It is biresident if
and only if, for both `nu=+,-`,

\[
\begin{aligned}
 G_d^\nu(P_1,A\to F,P_3),\\
 G_d^\nu(P_3,E\to D,P_2),\\
 G_d^\nu(P_2,C\to B,P_1)                               \tag{4.3}
\end{aligned}
\]

all hold.  It preserves the sum of the three old component voltages if and
only if

\[
 \delta(A,F)+\delta(C,B)+\delta(E,D)
 =\delta(A,B)+\delta(C,D)+\delta(E,F).                 \tag{4.4}
\]

Under a single coherent physical lift of the six Boolean-hex atoms,
(4.4) is automatic: the tail and head occurrence multisets agree, so their
phase potentials cancel.  Arbitrarily mixing separately canonicalized
quotient options does not justify this conclusion.

Consequently the merged component has voltage `epsilon` precisely when the
two nonpump old component voltages sum to zero.  In general its voltage is
their sum plus `epsilon`; zero relative displacement of A's two phases does
not replace this absolute condition.

The private closure `e_*`, its cap/history branch, and its orientation are
unchanged.  Thus the output exports the same pump private-edge state.

#### Proof

The four-resource Boolean-hex identity proves the inventory statement.
After deleting the old edges the three cycles are (4.2), and the new edges
concatenate them as

\[
 B\leadsto A\to F\leadsto E\to D\leadsto C\to B,
\]

so topology is one cycle.  Formula (4.3) is the exact connector recurrence
at the three and only three changed joins.  Additivity gives (4.4).  In a
coherent physical lift every edge displacement is head phase minus tail
phase, and equality of the typed tail/head multisets telescopes.  The target
edge was chosen away from `e_*`, so no private resource is touched.
\(\square\)

For the Cartesian hex through target

\[
 e=(L,U,E,F),\quad E=L+d_0,\quad F=L+a_0,
\]

the two free labels range over

\[
                         b\in L,qquad c\notin U.       \tag{4.5}
\]

At `k=2r-1` this gives exactly `(r-1)(r-2)` raw options.  If endpoint
guards forbid sets `B_L subset L` and `B_R subset [k]-U`, and a typed
forbidden bank `Q` deletes at most `lambda_Q` options in total, the exact
nonemptiness inequality is

\[
             (r-1-|B_L|)(r-2-|B_R|)>\lambda_Q.         \tag{4.6}
\]

For one fixed target, any fixed non-target lower, upper, tail, or head
resource occurs in at most `r-1` Cartesian options.  Hence the proof-safe
coarse estimate

\[
                         \lambda_Q\le |Q|(r-1)          \tag{4.7}
\]

may be used.  Coordinate labels are not capacity-one resources and must be
handled in `B_L,B_R`, not counted falsely in `Q`.

The six collar relations in (4.3) remain load-bearing even when (4.6)
holds.  A convenient strong sufficient state is that every newly paired
`I^nu(P_i)` and `D^nu(P_j)` is disjoint, the common hex deletion label is
absent from all positive predecessor collars and negative successor
collars, and each new insertion label is absent from its positive successor
and negative predecessor collar.  This is stronger than (4.3), but is a
literal finite prepared-state condition.

## 5. Available pump-edge count and parameter ledger

Each coordinate occurs exactly three times in the pump deletion stream and
three times in its insertion stream.  Therefore a coordinate-forbidden bank
`B` excludes at most `6|B|` of the `3k` pump edges.  Reserving the private
edge and a cyclic radius-`d` neighborhood excludes at most `2d+1` more.
Consequently a nonprivate candidate fusion edge exists whenever

\[
                         3k>6|B|+2d+1.                 \tag{5.1}
\]

The simultaneous local parameter requirements for the pump and A's
two-bank seven-ear collar are

\[
 r\ge\max\{3d+4,,2d+3\},\qquad
 k-r\ge2d+12.                                         \tag{5.2}
\]

For `k=2r-1`, this is

\[
                         r\ge\max\{3d+4,,2d+13\}.     \tag{5.3}
\]

Equations (4.6) and (5.1) are the additional, exact finite resource and
edge-supply inequalities.  They do not imply that the two partner old
atoms already lie on two distinct host components.  That is the prospective
Boolean-hex planting row.

## 6. Exact remaining host theorem

The strongest theorem justified by the current ingredients is therefore
conditional and sharply local:

> Choose one twisted pump branch and one fixed-`z` corridor state.  Plant
> their protected occurrence banks disjointly in an owner/lower-`q1` host.
> Retain the pump private edge.  Supply one coherent, zero-charge Boolean
> hex through another pump edge whose two partner edges lie on distinct
> host components and whose three connector collars satisfy (4.3).  Then
> the switch produces one component across those three cycles, preserves
> all immediate four-resource rows and preserves the exact pump state.  If
> the two nonpump component totals sum to zero, its absolute voltage is the
> chosen `epsilon`.  Every later
> completed fixed-`z` repair of zero displacement retains that voltage.

What remains unproved is precisely the prospective host statement in the
first two sentences.  Neither the small protected-factor theorem nor a
post-hoc two-edge splice supplies it.  A correct all-parameter theorem must
either

1. complete the developed pump plus corridor jointly in a quotient-aware
   owner/`q1` factor and expose the prepared hex partners; or
2. prove a residual `b`-factor/Ore--Ryser inequality after deleting the
   `3k` pump owners and facets, together with the history-compatible hex
   supply.

Deeper upper shadows, source/envelope rows, exterior all-width windows and
the terminal common-cap/compiler remain separate.
