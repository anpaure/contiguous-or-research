# The endpoint-corrected PBBS collar factor has a deterministic short-run obstruction

**Date:** 2026-08-13  
**Status:** unconditional no-go for the endpoint-corrected high graph face;
no computation or probabilistic argument.  The corrected four-incoming,
one-outgoing collar architecture remains a valid protected graph factor, but
its retained role-zero height spine makes that factor source-dead whenever
the displayed bad-height interval is nonempty.

## 1. Setting

Put

\[
 A_h=0\,1^h0^h(10)^{r-h},\qquad U_h=A_h^c,
\]

and retain the role-zero height-spine edges

\[
 e_t=U_tU_{t+1},\qquad
 U_{t+1}=U_t-\{t+1\}+\{2t+1\}                 \tag{1.1}
\]

for `4<=t<H`.  This is exactly the spine retained by the endpoint-corrected
four-incoming/one-outgoing collar bank.  Let the required owner-window width
be

\[
                         q=\delta+1.             \tag{1.2}
\]

The graph-level theorem protects every edge in (1.1), so every eventual
two-factor containing the bank must traverse each internal displayed spine
segment consecutively.  Reorienting a factor component can reverse such a
segment but cannot change its coordinate-run lengths.

## 2. Exact protected run

### Theorem 2.1 (deterministic short positive run)

For every

\[
 4\le h\le
 \min\!\left\{\delta,\left\lfloor\frac{H-1}{2}\right\rfloor\right\},
                                                               \tag{2.1}
\]

the coordinate `c=2h+1` has, on the protected height-spine segment, the
maximal positive owner run

\[
                     U_{h+1},U_{h+2},\ldots,U_{2h},             \tag{2.2}
\]

of length exactly `h<q`.  Consequently no spanning two-factor containing
the corrected protected bank has a depth-`delta` source antecedent.  This
remains true before any source pins, upper backups, cap choices, or component
fusion are imposed.

#### Proof

At `e_h`, (1.1) inserts `2h+1`, so `c` is absent from `U_h` and present in
`U_(h+1)`.  A later transition `e_t` removes coordinate `t+1`; hence it
first removes `c` when `t=2h`.  No transition strictly between `e_h` and
`e_(2h)` changes `c`.  Thus `c` is present precisely at the `h` consecutive
owners in (2.2), while the two adjacent owners `U_h` and `U_(2h+1)` omit it.
Condition (2.1) ensures that both boundary edges belong to the retained
spine.  The run is therefore maximal and has length `h<=delta<q`.

Every one of its consecutive incidences is protected.  A completing factor
cannot insert another owner inside the run, remove either boundary, or extend
the run through either adjacent owner.  Reversing its orientation preserves
its length.  But in any width-`q` source representation

\[
                 T_i=\bigcup_{j=i}^{i+q-1}A_j,                 \tag{2.3}
\]

each positive owner incidence of `c` must be covered by a source occurrence
whose complete `q`-owner window contains `c`.  No such window fits inside a
maximal positive run of length below `q`.  Equation (2.3) is impossible.
\(\square\)

### Corollary 2.2 (age-filtered Hall is empty before Hall)

Fix any matching phase and any capped-age labelling for a proposed
`q`-resident completion.  The protected successor which deletes `c` at
`e_(2h)` is age-illegal: the current positive age of `c` is exactly `h<q`.
Therefore the forced-arc set is not even contained in the age-filtered
successor graph.  No Hall-surplus estimate can repair the face.

### Corollary 2.3 (unpinned erosion failure)

In the pinned-erosion criterion, take the pin set empty.  For every owner
inside (2.2), there is no safe source position in its width-`q` emission
window for coordinate `c`.  Thus the coordinate-coverage row fails already
on the nominal unpinned trace.

## 3. Quantitative consequence and mandatory redesign

The first bad height is `h=4`.  Hence the obstruction is present whenever

\[
                         \delta\ge4,\qquad H\ge9.               \tag{3.1}
\]

More generally, (2.1) gives one forced short run for every such `h`; these
are deterministic coordinate/age cuts, not defects caused by marginal
packing or arbitrary completion.

Any viable synchronized-collar source architecture must therefore break at
least one boundary of each interval

\[
                         \{e_h,e_{h+1},\ldots,e_{2h}\}.          \tag{3.2}
\]

Deleting the low role-zero spine does exactly this but opens the fifth
common-history/current route.  The alternative is a fused or shared
role-zero collar which *replaces* a spine incidence and carries the adjacent
height through a resident detour.  Appending a collar while retaining the
whole spine cannot work: the all-five incoming bank then has degree three,
whereas omitting that collar leaves Theorem 2.1 unchanged.

Thus the next local gate is not pinned erosion on the corrected graph face.
It is an explicit shared-incidence role-zero replacement preserving, in one
object, owner/`q1` simplicity, the fifth common-history occurrence route,
and the required cumulative-union exterior profile.
