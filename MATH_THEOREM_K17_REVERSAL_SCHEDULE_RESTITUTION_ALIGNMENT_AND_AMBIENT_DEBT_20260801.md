# The k=17 reversal schedules place the restitution triangle exactly, but do not pay the 12--18 ambient deck debt

**Date:** 2026-08-01  
**Status:** exact schedule/cell identity and exact no-go for obtaining an
additional gain merely by choosing the reflected representative.  The new
all-fourteen-cut q1 factor result permits a minimum-loss packet cut.  The
new twin-Ferrers-bank theorem supplies all twelve missing upper witnesses
with `5d` protected owners in its stable range.  A later explicit h=2
redesign now realizes those owners literally at k=17 and embeds the complete
29-owner protected system in an upper-q1-complete seven-factor.  That factor
still fails residence and deeper upper coverage, and no lower compiler is
asserted.

## 0. Outcome

For `k=17`, put

\[
 r=9,\qquad W=\binom{17}{9}=24310,\qquad d=3,
 \qquad L=W+d=24313,
\]

and let `a=7401` be the exact lower-layer slack spent by the one-jump
schedule.

The late-deadline representative is

\[
 G=(W,W,W),\qquad H=(0,0,a),                         \tag{0.1}
\]

and its reflected early-start representative is

\[
 G^*=(W-a,W,W),\qquad H^*=(0,0,0).                   \tag{0.2}
\]

The three source cells in the canonical depth-three restitution tail fit
the physical staircase **exactly**:

* in (0.1), their six proper derivative occurrences are the six terminal
  triangular cells on physical positions `W,W+1,W+2`;
* in (0.2), their reflections are the six initial triangular cells on
  physical positions `0,1,2`.

Thus the occurrence restitution charge `3+2+1=6` costs no cell outside the
optimal k=17 lower atlas, provided the packet is placed at the corresponding
global end.

The packet's canonical three-cell tail still has between 12 and 18 missing
cyclic-deck targets, depending on the packet cut.  All fourteen cuts now
have an exact q1 two-factor host.  Six cuts attain the minimum 12, so q1
does not prevent choosing a best cut.  However all twelve remaining targets
at a best cut have rank at least ten.  They cannot be represented by the
strict-lower triangular cells.  Reflection preserves their ambient-deficit
function occurrence by occurrence.

The later twin-bank theorem changes the next line, but not this schedule
calculation.  It identifies the twelve values as two Ferrers triangles and
constructs two paths on `2d+3d=5d` owners which duplicate them without any
new word positions.  Thus the ambient debt is locally repayable by protected
owner resources, not by the six lower boundary cells.

Consequently:

\[
 \boxed{\text{late versus early orientation alone gives no reduction below
 the audited minimum ambient debt }12.}                 \tag{0.3}
\]

Likewise, reflection cannot lower a terminal compiler deficiency or the
separate `43 -> 25`, deficiency-18 provider aperture: it gives an isomorphic
target--cell or target--provider graph.

## 1. Exact owner supports in the two schedules

For (0.1), the omitted physical starts and deadlines are

\[
 X=\{W,W+1,W+2\},\qquad Y=\{0,1,a+2\}=\{0,1,7403\}. \tag{1.1}
\]

The selected owner indexed by `i` has support

\[
 I_i^+=
 \begin{cases}
 [i,i+2],&0\le i<a,\\
 [i,i+3],&a\le i<W.
 \end{cases}                                           \tag{1.2}
\]

For (0.2),

\[
 X^*=\{W-a,W+1,W+2\}=\{16909,24311,24312\},
 \qquad Y^*=\{0,1,2\},                                \tag{1.3}
\]

and

\[
 I_j^-=
 \begin{cases}
 [j,j+3],&0\le j<W-a,\\
 [j+1,j+3],&W-a\le j<W.
 \end{cases}                                           \tag{1.4}
\]

Let

\[
 \rho(p)=L-1-p=W+2-p.                                  \tag{1.5}
\]

The owner index transforms as `j=W-1-i`.  If `i<a`, then

\[
 \rho([i,i+2])=[W-i,W+2-i]=[j+1,j+3],                  \tag{1.6}
\]

while if `i>=a`,

\[
 \rho([i,i+3])=[W-1-i,W+2-i]=[j,j+3].                  \tag{1.7}
\]

Equations (1.6)--(1.7) are the literal row-by-row identity between the
shallow prefix in (0.1) and the shallow suffix in (0.2).

## 2. The complete lower atlases are reflections

The late schedule has the exact address atlas

\[
\begin{aligned}
 {\cal C}_+=
 &\{[i,i],[i,i+1]:0\le i<a\}\\
 &\cup\{[i,i],[i,i+1],[i,i+2]:a\le i<W\}\\
 &\cup\{[t,u]:W\le t\le u\le W+2\}.                  \tag{2.1}
\end{aligned}
\]

Its size is

\[
 2a+3(W-a)+\binom42=3W-a+6=65535.                      \tag{2.2}
\]

The reflected address atlas is

\[
\begin{aligned}
 {\cal C}_-=
 &\{[i,i],[i,i+1],[i,i+2]:0\le i\le W-a\}\\
 &\cup\{[i,i],[i,i+1]:W-a+1\le i\le W+1\}\\
 &\cup\{[W+2,W+2]\}.                                  \tag{2.3}
\end{aligned}
\]

Direct endpoint reflection gives

\[
 \boxed{\rho({\cal C}_+)={\cal C}_-.}                  \tag{2.4}
\]

Both atlases have exactly one cell for every nonempty target below rank
nine.  Their scalar surplus is zero.  A compatible pin contraction removes
one target and one cell and is scalar-neutral; it creates no free address.

## 3. Exact identity with the three-cell restitution tail

Put

\[
 {\cal R}_+=\{[W+i,W+j]:0\le i\le j\le2\}.             \tag{3.1}
\]

This is precisely the terminal triangular bank in the last line of (2.1).
At derivative depths `q=0,1,2`, it contains respectively

\[
 3,\quad2,\quad1                                         \tag{3.2}
\]

cells.  These are exactly the wrap-restoration occurrence counts for the
canonical depth-three source tail.

At the natural packet cut, the restitution cells are the first three states
`A_0,A_1,A_2` of the literal source transporter.  They all have rank six,
successive states make a Johnson exchange, and therefore the six cells in
(3.1) have rank histogram

\[
 6^3,\qquad7^2,\qquad8^1.                               \tag{3.3}
\]

Their reflected bank is

\[
 {\cal R}_-=\rho({\cal R}_+)
   =\{[i,j]:0\le i\le j\le2\},                          \tag{3.4}
\]

the initial triangle in (2.3).  Thus a terminal packet tail in the late
representative and the corresponding initial reversed tail in the early
representative use exactly the same six lower occurrences.

This proves a positive but sharply scoped conclusion: no six-cell ambient
sidecar is needed for derivative-row restitution.  The six target values
must still be included in the one bijective lower compiler.

## 4. The 12--18 target-support debt is disjoint from that triangle

The exact all-cut audit

```text
scratch/r2_k17_reset_open_ml9_ffactor_20260801/run.cuts.tsv
```

gives the full missing cyclic-deck counts after appending the canonical
three-cell tail:

\[
 18,18,15,12,12,12,15,18,18,15,12,12,12,15.             \tag{4.1}
\]

Hence the six best cuts are

\[
 c\in\{3,4,5,10,11,12\}.                                \tag{4.2}
\]

At every best cut the exact missing-rank histogram is

\[
 10^1,\quad11^2,\quad12^3,\quad13^1,\quad14^2,\quad15^3,
                                                               \tag{4.3}
\]

totalling twelve.  The first three are the unavoidable short-family
residual `10^1 11^2`; the other nine are longer-interval losses for this
literal packet.

Every value in (4.3) has rank above the middle rank nine.  Every cell in
`C_+` and `C_-` is strict-lower.  Therefore

\[
 \boxed{
  \text{no triangular lower cell can serve any of the twelve ambient
  packet losses in (4.3).}}                              \tag{4.4}
\]

The exact ambient criterion remains

\[
 N_+(T)\ge\mu_c(T)\qquad\text{for every packet target }T. \tag{4.5}
\]

Under whole-word reflection,

\[
 \mu_{c^*}^{\operatorname{rev}A}(T)=\mu_c^A(T),
 \qquad N_-(T)=N_+(T).                                  \tag{4.6}
\]

For the canonical source indexing, reversal sends the cut parameter to

\[
 c^*\equiv1-c\pmod {14}.                                \tag{4.7}
\]

Indeed `A_i^-=A_(3-i)^+`, and reversing

\[
 (A_c,\ldots,A_{c+13},A_c,A_{c+1},A_{c+2})
\]

is the canonical restitution word in the minus phase beginning at
`c*=1-c`.  The best cut orbits are

\[
 \{3,12\},\qquad\{4,11\},\qquad\{5,10\}.               \tag{4.8}
\]

Thus orientation does not turn a twelve-loss cut into a smaller-loss cut.

## 5. What the new all-fourteen-cut q1 factor result changes

The authenticated audit

```text
scratch/r2_k17_reset_open_ml9_ffactor_20260801/run.audit.json
```

proves that every one of the fourteen packet cuts extends to a spanning
degree-two factor of `ML_9` with the common 26-edge packet path fixed.  In
particular, the q1 owner/lower-incidence gate does not force use of a
15- or 18-loss cut: one may choose any cut in (4.2).

This is real progress.  It sharpens the packet-local ambient bank from the
range `12--18` to the attainable minimum `12` at the q1-factor level.

It does not prove that the factor:

* is one component or admits the required global opening;
* has the complete higher upper deck;
* has a literal depth-three source with legal exterior joins;
* supplies the twelve witnesses in (4.3); or
* has a common lower compiler.

The factor component count in the audit is still between 3159 and 3172.
The exact schedule alignment of Section 3 becomes usable only if the chosen
packet path is placed at the corresponding global end of the final
one-component source chronology.

## 6. Exact placement of the new `5d` twin bank in the particle schedule

The theorem

```text
MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md
```

uses a `2d`-owner path `P_X` and a `3d`-owner path `P_U`.  For d=3 these
have six and nine owners, respectively.  Its two upper triangles have
exactly the histogram (4.3), so they are the complete twelve-target leave
of a minimum-loss packet cut.

There is no address-capacity obstruction in either k=17 representative.
In the late schedule, reserve the terminal deep-owner block as

\[
\begin{array}{c|c|c}
\text{path}&\text{owner indices}&\text{count}\\ \hline
P_X&W-29,\ldots,W-24&6\\
P_U&W-23,\ldots,W-15&9\\
\text{opened packet}&W-14,\ldots,W-1&14.
\end{array}                                               \tag{6.1}
\]

All these indices exceed `a=7401`, so every support is the flat
four-position interval `[i,i+3]`.  The packet source occupies the final
`14+3` physical positions and its three overlap cells are exactly the
terminal triangle in (3.1).

Under the owner reflection `j=W-1-i`, (6.1) becomes

\[
\begin{array}{c|c|c}
\text{path}&\text{owner indices}&\text{count}\\ \hline
\text{opened packet}&0,\ldots,13&14\\
P_U&14,\ldots,22&9\\
P_X&23,\ldots,28&6.
\end{array}                                               \tag{6.2}
\]

Every one of these indices lies below `W-a=16909`, so again every support
is `[j,j+3]`.  The reflected three-cell overlap is the initial triangle
(3.4).  Even the optional `2d=6` residence-collar owners fit immediately
after (6.2), at indices 29 through 34.

Therefore

\[
 \boxed{\text{the reflected early-start schedule can place all }5d=15
 \text{ protected bank owners, with no particle loss.}}   \tag{6.3}
\]

The uniform four-marker proof does not apply directly at k=17: its normal
form has

\[
 h=r-2d-1=9-6-1=2,                                      \tag{6.4}
\]

whereas its collision-separation theorem assumes four distinct permanent
markers in `H`, i.e. `h>=4`.  There is only one coordinate outside the
sixteen-coordinate packet support, so the current proof does not obtain
four permanent marker signatures by borrowing unused coordinates.  Also,
the general protected-factor corollary requires `m>=22d`; here `m=9` and
`22d=66`.

Nevertheless, the separate theorem

```text
MATH_THEOREM_K17_H2_TWIN_FERRERS_BANK_AND_PROTECTED_ML9_FACTOR_20260801.md
```

provides exactly the missing finite redesign.  It gives 15 explicit h=2
bank owners, proves all 29 packet-plus-bank owners and all 26 protected
lower/upper q1 colours distinct, and embeds all 52 protected incidence edges
in an upper-q1-complete spanning factor with seven components.  Hence the
marker and combined q1-factor gates are now closed at k=17; (6.1)--(6.3)
give their compatible physical schedule placement.

## 7. What simplifies in the fixed-`M_0` rooted correlation

There is a genuine local simplification once a protected combined factor
exists.  Let

\[
 Z_0-Z_1-\cdots-Z_s
\]

be any one of the packet or twin-bank Johnson paths, with lower colours

\[
 I_i=Z_i\cap Z_{i+1}.
\]

Alternately colour its incidence lift so
that

\[
 M_0(I_i)=Z_i,
 \qquad e_i=I_iZ_{i+1}\in M_1.                            \tag{7.1}
\]

For the upper q1 colour `U_i=Z_i union Z_(i+1)`, the tail and head are then
fixed:

\[
 \psi(U_i)=Z_i,\qquad\phi(U_i)=Z_{i+1}.                   \tag{7.2}
\]

The associated rooted Catalan link is

\[
 \lambda(e_i)=\{I_i,M_0^{-1}(Z_{i+1})\}.
\]

For `i<s-1`, this is `I_i I_(i+1)`.  At the last edge it is `I_(s-1) J`,
where `J=M_0^{-1}(Z_s)` lies outside the protected lower bank.  Hence every
protected owner path projects to the literal forest path

\[
 I_0-I_1-\cdots-I_{s-1}-J.                               \tag{7.3}
\]

So, on the protected seed:

* tail injectivity and head injectivity are automatic;
* the upper-q1 colours are already distinct;
* the rooted links are graphic-independent;
* the two Ferrers triangles need no fixed-`M_0` selection at all, because
  their non-q1 targets are witnessed by longer intervals wholly inside
  `P_X` and `P_U`.

For d=3 only one member of the twelve-target leave has rank ten; the other
eleven have ranks 11 through 15.  Thus the twin construction removes those
eleven demands from the Catalan q1 correlation entirely.  The q1 edges of
the bank merely form the explicit forest seed (7.3).

This does **not** solve the global fixed-`M_0` problem.  One still must:

1. extend all protected incidences to one spanning factor;
2. choose the remaining upper colours while keeping tails and heads
   injective;
3. keep the full contracted link graph acyclic and connectible in the
   required way; and
4. retain the literal source, exterior upper witnesses, and common compiler.

At k=17, the explicit h=2 theorem makes this protected seed literal.  It
converts the two upper triangles from a support problem into a small
protected-forest seed problem; it does not remove the global rooted
lower/head/graphic correlation.

## 8. Separate deficiencies are also reversal-invariant

Let `G_comp` be any occurrence-labelled lower target--cell graph for one
oriented word.  Reflect every cell address.  This is a graph isomorphism

\[
 G_{\rm comp}^+\cong G_{\rm comp}^-.                     \tag{6.1}
\]

It preserves matching rank and every Dulmage--Mendelsohn deficiency.  At
the k=17 one-pivot schedule, where `|C|=Lambda_17`, the graph is tight in
both representatives.

Likewise, in the fixed-r3 provider audit, reflect every witness footprint
and every one-capacity owner position.  The 43-target family still injects
through a 25-position aperture, so

\[
 43-25=18                                                \tag{6.2}
\]

is unchanged.  A different owner factor or a different correlated provider
bank may remove that obstruction; choosing (0.1) rather than (0.2) cannot.

## 9. Exact frontier

The k=17 quotient-state audit therefore gives one positive identity and one
no-go:

\[
 \boxed{
 \begin{array}{l}
 \textbf{Positive: }\text{the three physical restitution letters and all
 six derivative occurrences fit exactly in the staircase triangle;}\\[2mm]
 \textbf{No-go: }\text{reflection only relocates this triangle and
 transports every remaining ambient/compiler deficiency isomorphically.}
 \end{array}}                                            \tag{7.1}
\]

After using the all-fourteen-cut q1 factor result to select a best cut, the
h=2 twin-Ferrers theorem gives a literal one-oriented ambient witness bank
and a combined upper-q1-complete seven-factor.  The next theorem is not
another orientation or marker choice: it must repair the frozen factor's
5760 post-opening short runs and 1806 deeper upper holes, or find a better
protected factor, before exposing one literal tight lower compiler.  Global
reflection then supplies the opposite representative for free.
