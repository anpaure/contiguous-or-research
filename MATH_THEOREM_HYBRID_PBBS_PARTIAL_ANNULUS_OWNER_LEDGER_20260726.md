# Hybrid PBBS/partial-annulus baseline audit: an exact overlay obstruction and a common-successor ledger

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

After putting the two constructions on one common parity while retaining
their designated witnesses, the currently proved fixed-annulus
partial-SCD word and the currently proved sub-Gaussian PBBS word do
**not** fuse in place as atom-preserving templates.

There are three separate reasons, with different scopes.

1.  In the partial-SCD compiler, the (W-N_{q_0}) unused middle owners
    are appended as one-letter witnesses.  Any common master word of
    length (W+e) which preserves both these one-letter witnesses and the
    canonical multi-letter PBBS middle witnesses must satisfy

    \[
       2e\ge W-N_{q_0}.
       \tag{0.1}
    \]

    At a fixed Gaussian entrance (q_0=a\sqrt m+O(1)), this is a
    positive linear excess.

2.  Even if the PBBS template is forgotten, the standalone partial-SCD
    word has a linear shallow deficit.  If its provider states have a
    (p)-path rotor cover, then at every (1\le s<q_0)

    \[
       h_s^-\ge N_s-N_{q_0}-2Hp-E_{\rm rep}.
       \tag{0.2}
    \]

    Hence, for (s=o(\sqrt m)), (p=o(W/H)), and
    (E_{\rm rep}=o(W)),

    \[
       h_s^-\ge (1-e^{-a^2}-o(1))W.
       \tag{0.3}
    \]

    Adding only the (o(W)) auxiliary part of the PBBS word cannot
    repair this.

3.  Conversely, retaining the PBBS principal erosion letters while
    adding an annular compiler is impossible by endpoint capacity: at
    least

    \[
       N_{q_0}-o(W)=(e^{-a^2}-o(1))W
       \tag{0.4}
    \]

    PBBS principal positions must be rewritten.

Thus a no-second-baseline fusion, if it exists, is necessarily a
**wholesale common-chronology rethreading**.  The new morphological
preimage theorem is exactly the right literal mechanism for such a
rewrite: one (W)-position erosion word can retain all middle owners and
both trace towers.  It does not, however, align the fixed SCD providers
with PBBS endpoints.

This note gives the exact positive ledger for that remaining possibility.
On a common owner set, let (P) be the reference PBBS successor factor
and (F) an (H)-safe successor factor which realizes the fixed-annulus
SCD flags.  Put

\[
   e=|E(P)\setminus E(F)|.
   \tag{0.5}
\]

In even dimension, the PBBS shallow support lost through depth (h) is
at most

\[
   h(h+1)e.
   \tag{0.6}
\]

In the direct odd convention, including the shifted upper windows, it is
at most

\[
   (h+1)^2e.
   \tag{0.7}
\]

Consequently a common factor with (C) components gives a genuine
one-baseline hybrid word of length

\[
 \boxed{
 W+2HC+h(h+1)e+\Gamma_{h,q_0}}
 \tag{0.8}
\]

in even dimension, where \(\Gamma_{h,q_0}\) is the actual two-sided
support deficit in the uncontrolled gap (h<q<q_0).  The direct odd
analogue is

\[
 \boxed{
 W+(2H+1)C+(h+1)^2e+\Gamma_{h,q_0}^{\rm odd}.}
 \tag{0.9}
\]

The exact fixed-SCD common-endpoint Hall condition in Section 5 makes the
scheduled annular term zero.  It is not claimed necessary for every
unrestricted use of all other intervals in the resulting word.

The present partial-SCD theorem proves neither a full common owner factor,
nor an (o(W/h^2)) edit bound relative to PBBS, nor the gap estimate, and
its native parity differs from the PBBS theorem.  Therefore the audit does
not prove coefficient one.  It proves a linear obstruction to direct
fusion and isolates a sharp quantitative wholesale-fusion gate.

## 1. Endpoint flags and rigidity of two middle-witness systems

Let

\[
   Q=(Q_1,\ldots,Q_L)
   \tag{1.1}
\]

be a nonempty literal OR word.  If intervals with the same right endpoint
are ordered by inclusion, their unions are ordered by inclusion.  The
same is true for intervals with a common left endpoint.

### Lemma 1.1 (one antichain target per endpoint)

Let \(\mathcal A\) be an antichain of subsets of the ground set.  In any
chosen family of witnesses, one for each member of \(\mathcal A\), the
right endpoints are distinct and the left endpoints are distinct.

#### Proof

Two intervals with a common right endpoint are nested, so their unions
are comparable.  Two comparable members of an antichain are equal.
Therefore two distinct targets cannot use the same right endpoint.  The
left-endpoint statement is identical. \(\square\)

The next lemma is an exact baseline-sharing statement which uses no
cardinality information about the letters.

### Theorem 1.2 (common-interval rigidity)

Let \(\mathcal A\) be an antichain of size \(W\).  Suppose a word of
length

\[
   L=W+e
   \tag{1.2}
\]

contains two designated witness systems

\[
   (I_X:X\in\mathcal A),\qquad
   (J_X:X\in\mathcal A).
   \tag{1.3}
\]

Then at least \(W-e\) targets have the same right endpoint in the two
systems, at least \(W-e\) have the same left endpoint, and at least

\[
   \boxed{W-2e}
   \tag{1.4}
\]

have exactly the same witness interval.

Consequently, if \(I_X\) is a singleton interval for \(r\) targets while
the corresponding \(J_X\)'s are all nonsingleton, then

\[
   \boxed{e\ge r/2.}
   \tag{1.5}
\]

#### Proof

By Lemma 1.1, the two right-endpoint maps inject \(\mathcal A\) into
\([L]\).  Their images each have size \(W\), and hence intersect in at
least

\[
   2W-L=W-e
   \tag{1.6}
\]

positions.  If \(I_X\) and \(J_Y\) have the same right endpoint, their
unions are comparable.  Since both belong to \(\mathcal A\), they are
equal, so \(X=Y\).  This proves the right-endpoint assertion.  The
left-endpoint assertion is identical.

Intersect the two sets of targets just obtained.  Their intersection has
size at least \(W-2e\), and on it both endpoints agree, so the complete
intervals agree.  A singleton and a nonsingleton interval cannot agree;
therefore all \(r\) exceptional targets lie outside a set of size at most
\(2e\).  This proves (1.5). \(\square\)

The theorem remains valid for an atom-preserving overlay **provided the
cap condition is imposed**: every designated source interval must remain
an exact witness after foreign atoms are inserted between its embedded
endpoints.  Under this condition the two embedded interval families are
witness systems in the master word, so Theorem 1.2 applies.  Without the
cap condition a foreign atom may enlarge a target, and no overlay claim
is justified.

## 2. Direct atom-preserving PBBS/partial-SCD overlay is impossible

We first work in any common parity in which the two templates have been
placed on the same middle layer.  The current partial-SCD theorem is
native on \([2m]\), while the current PBBS theorem is native on
\([2m+1]\); this typing issue is audited separately in Section 8.

In the partial-SCD path-forest compiler, precisely \(N_{q_0}\) middle
owners are chronologized as provider states.  Every other middle owner is
appended as one literal set-letter.  Thus the template has

\[
   r=W-N_{q_0}
   \tag{2.1}
\]

designated singleton middle witnesses.

On a residence-safe PBBS path, the canonical delayed-atom witness for an
internal middle owner is never a singleton.  To see this, let

\[
   B_j=\bigcap_{u=0}^{d}M_{j-u},\qquad d\ge1,
   \tag{2.2}
\]

on an owner-simple row satisfying the positive-delay hypothesis \(P_d\).
The middle identity is

\[
   M_i=\bigcup_{j=i}^{i+d}B_j.
   \tag{2.3}
\]

Every atom in this interval is contained in \(M_i\) and in at least one
other, distinct equal-rank owner.  Hence every nonempty such atom is a
proper subset of \(M_i\).  Formula (2.3) therefore needs at least two
nonempty atoms.  After empty atoms are deleted, the designated PBBS
middle interval still has two distinct endpoints.

This argument must not be used across a short PBBS residence.  In the
audited PBBS compiler, cut \(J\) transition edges meeting every positive
residence of length at most \(d\), and use endpoint-capped erosion on the
resulting paths.  At most

\[
   z_P\le(d+1)J
   \tag{2.3a}
\]

middle-owner windows meet a cut.  Every other owner has the nonsingleton
canonical witness just proved.  For the unconditional sub-Gaussian
compiler,

\[
   d=h+1,\qquad J=O(B\sqrt m),\qquad W=(2m+1)B,
   \tag{2.3b}
\]

so \(h=o(\sqrt m)\) gives

\[
   z_P=O(Bh\sqrt m)=o(W).
   \tag{2.3c}
\]

Apply Theorem 1.2 to the middle-layer antichain.  Among the
\(W-N_{q_0}\) singleton partial-SCD witnesses, at most \(z_P\) can be
PBBS exceptions.  Any capped master overlay preserving both designated
systems therefore has

\[
   \boxed{
   L\ge W+\frac{W-N_{q_0}-z_P}{2}.}
   \tag{2.4}
\]

In particular,

\[
   L\ge W+\frac{W-N_{q_0}-o(W)}2.
   \tag{2.4a}
\]

For the even middle layer,

\[
   W=\binom{2m}{m},\qquad
   N_q=\binom{2m}{m-q},
   \tag{2.5}
\]

and, for \(q_0=a\sqrt m+O(1)\),

\[
   \frac{N_{q_0}}W=e^{-a^2+o(1)}.
   \tag{2.6}
\]

Thus (2.4a) becomes

\[
   \boxed{
   L\ge
   \left(1+\frac{1-e^{-a^2}}2-o(1)\right)W.}
   \tag{2.7}
\]

This proves a genuine no-go for a common-parity capped overlay preserving
the two existing designated templates, up to the explicitly charged
\(o(W)\) PBBS cut neighborhood.  It does not apply after the singleton
owner positions are replaced by small morphological atoms; that operation
deliberately abandons the partial template's singleton witnesses.

## 3. The partial-SCD word has a linear shallow deficit

Return to the native even notation (2.5), and put

\[
   q_0=\lceil a\sqrt m\rceil,\qquad
   H=\lfloor b\sqrt m\rfloor,
   \qquad 0<a<b.
   \tag{3.1}
\]

Suppose the \(N_{q_0}\) providers have a radius-\(H\) rotor path cover
with \(p\) paths.  Its hard-started packet blocks use at most

\[
   N_{q_0}+2Hp
   \tag{3.2}
\]

positions.  Append the other \(W-N_{q_0}\) middle owners as rank-
\(m\) singleton letters, and allow \(E_{\rm rep}\) further positions.

### Theorem 3.1 (exact shallow endpoint deficit)

For every \(1\le s<q_0\), the number \(h_s^-\) of uncovered rank-
\((m-s)\) targets satisfies

\[
   \boxed{
   h_s^-\ge
   N_s-N_{q_0}-2Hp-E_{\rm rep}.}
   \tag{3.3}
\]

#### Proof

No interval with union of rank \(m-s\) can end at one of the appended
rank-\(m\) letters, because the interval contains its endpoint letter.
By Lemma 1.1, every other endpoint witnesses at most one distinct target
of rank \(m-s\).  There are at most

\[
   N_{q_0}+2Hp+E_{\rm rep}
\]

such endpoints.  Subtracting this upper bound from the \(N_s\) targets
proves (3.3). \(\square\)

Uniformly for \(q=O(\sqrt m)\),

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1},
 \qquad
 \log\frac{N_q}{W}
 =-\frac{q^2}{m}+O\!\left(\frac q m+\frac{q^3}{m^2}\right).
 \tag{3.4}
\]

Consequently, if \(s=o(\sqrt m)\), \(p=o(W/H)\), and
\(E_{\rm rep}=o(W)\), then

\[
   N_s=(1-o(1))W,qquad
   N_{q_0}=(e^{-a^2}+o(1))W,
   \tag{3.5}
\]

and (3.3) gives (0.3).

The assertion is stronger than saying that the current theorem has no
shallow ledger: it proves that its literal singleton completion cannot
possibly have an \(o(W)\) shallow ledger at a fixed Gaussian entrance.
Those singleton positions must be rewritten, not merely supplemented by
the \(o(W)\) PBBS auxiliary positions.

## 4. Sparse modification of the PBBS baseline is also impossible

The obstruction in the opposite direction is equally elementary.  Work
on the odd PBBS ground set \([2m+1]\), and put

\[
   W_o=\binom{2m+1}{m},\qquad
   D_q=\binom{2m+1}{m-q}.
   \tag{4.1}
\]

The PBBS compiler for a central half-width \(h=o(\sqrt m)\) uses radius
\(h+1\).  Each of its \(W_o\) principal erosion letters has size at
least

\[
   m+1-(h+1)=m-h.
   \tag{4.2}
\]

Fix \(q_0>h\).  These letters are strictly larger than a rank-
\((m-q_0)\) target.

### Theorem 4.1 (annular endpoint rewrite bill)

Suppose a new word retains all but \(K\) principal PBBS letters, has
\(E\) old auxiliary positions, and inserts \(R\) new positions.  If it
covers rank \(m-q_0\), then

\[
   \boxed{K+E+R\ge D_{q_0}.}
   \tag{4.3}
\]

#### Proof

Every rank-\((m-q_0)\) witness has a distinct right endpoint by
Lemma 1.1.  It cannot end at an unchanged principal letter by (4.2).
Only the \(K+E+R\) other positions are eligible. \(\square\)

For fixed \(a>0\) and \(q_0=a\sqrt m+O(1)\),

\[
   \frac{D_{q_0}}{W_o}
   =\prod_{j=0}^{q_0-1}\frac{m-j}{m+2+j}
   =e^{-a^2+o(1)}.
   \tag{4.4}
\]

Since the PBBS auxiliary count is \(E=o(W_o)\), a length-
\(W_o+o(W_o)\) fusion requires (0.4).  Thus neither existing baseline can
be retained sparsely.

## 5. What the morphological rewrite actually proves

Let \((M_t)\) be a disjoint union of cyclic rank-\(m\) Johnson rows on
\([2m]\), enumerating all \(W\) middle owners once.  Assume every segment
of at most \(H+1\) transitions is geodesic.  In particular every positive
coordinate residence has length at least \(H+1\).  Define

\[
   R_t=\bigcap_{i=0}^{H}M_{t+i},
   \tag{5.1}
\]

with indices taken inside each cycle, and put

\[
   \Phi_q^-(t)=\bigcap_{i=0}^{q}M_{t+i},\qquad
   \Phi_q^+(t)=\bigcup_{i=0}^{q}M_{t+i}.
   \tag{5.2}
\]

### Theorem 5.1 (one-baseline two-sided erosion identity)

For every \(0\le q\le H\),

\[
   |R_t|=m-H,
   \tag{5.3}
\]

\[
   \boxed{
   \bigcup_{j=t-H+q}^{t}R_j=\Phi_q^-(t),}
   \tag{5.4}
\]

and

\[
   \boxed{
   \bigcup_{j=t-H}^{t+q}R_j=\Phi_q^+(t).}
   \tag{5.5}
\]

In particular, the \(H+1\)-letter interval in (5.4) at \(q=0\) is
exactly \(M_t\).  Linearizing a component by copying its first \(2H\)
letters preserves every displayed cyclic witness.  If there are \(C\)
components, the resulting core word has length at most

\[
   W+2HC.
   \tag{5.6}
\]

#### Proof

Geodesicity makes the next \(H\) deleted coordinates distinct members of
\(M_t\), proving (5.3).  For (5.4), parse one coordinate residence as an
integer interval \([a,b]\).  The coordinate belongs to \(R_j\) exactly
when

\[
   [j,j+H]\subseteq[a,b],
   \quad\text{equivalently}\quad
   a\le j\le b-H.
   \tag{5.7}
\]

This occurrence interval meets \([t-H+q,t]\) exactly when
\(a\le t\) and \(t+q\le b\), which says that the coordinate belongs to
every \(M_t,\ldots,M_{t+q}\).  This proves (5.4).

A coordinate which is positive around the whole cyclic component belongs
to every set on both sides, and a constant-zero coordinate belongs to
neither; thus the lifted-run argument covers all cyclic cases.

For (5.5), use the middle identity and expand:

\[
 \bigcup_{i=0}^{q}M_{t+i}
 =\bigcup_{i=0}^{q}\ \bigcup_{j=t+i-H}^{t+i}R_j
 =\bigcup_{j=t-H}^{t+q}R_j.
 \tag{5.8}
\]

The largest interval used in (5.5) has \(2H+1\) letters, so copying the
first \(2H\) letters of a cyclic block suffices and proves (5.6).
\(\square\)

This theorem constructs a new word.  It enlarges valid sparse
morphological seeds, but it does not preserve arbitrary old PBBS
dominance-staircase or cut-chart intervals.  It preserves precisely the
owner-derived traces in (5.4)--(5.5).

### 5.1 Exact fixed-SCD common-endpoint condition

Fix a full SCD \(\mathcal D\) of \(B_{2m}\).  Let

\[
   \Omega=\mathcal D_{\ge q_0}
   \tag{5.9}
\]

be the \(N_{q_0}\) retained providers, and write their paired flags as

\[
 D_q(C)\subset D_{q-1}(C),\qquad
 E_{q-1}(C)\subset E_q(C).
 \tag{5.10}
\]

Put \(h(C)=\min\{\rho(C),H\}\).  Define the fixed-chronology
compatibility graph \(\mathcal G_H(M,\mathcal D)\) between
\(\Omega\) and the \(W\) owner endpoints by

\[
 C\sim t
 \quad\Longleftrightarrow\quad
 \begin{cases}
 \Phi_q^-(t)=D_q(C),\\
 \Phi_q^+(t)=E_q(C)
 \end{cases}
 \quad(q_0\le q\le h(C)).
 \tag{5.11}
\]

### Theorem 5.2 (exact fixed-SCD fusion Hall theorem)

The **designated trace intervals** (5.4)--(5.5) of the erosion word
realize all prescribed depth-\(\ge q_0\) annular flags of the fixed SCD,
with owner-simple (possibly reassigned) middle corners, if and only if
\(\mathcal G_H(M,\mathcal D)\) has a matching saturating \(\Omega\),
equivalently if and only if

\[
   \boxed{
   |N_{\mathcal G_H}(\mathcal C)|\ge|\mathcal C|
   \quad(\mathcal C\subseteq\Omega).}
   \tag{5.12}
\]

#### Proof

An assignment of provider \(C\) to endpoint \(t\) realizes its annular
flag if and only if every equality in (5.11) holds, by Theorem 5.1.
Distinct assigned endpoints give distinct middle owners because the
chronology is owner-simple.  Thus a simultaneous assignment is exactly a
matching saturating \(\Omega\).  Hall's theorem gives (5.12).
\(\square\)

If one insists on the original SCD middle corner and its shallow inner
flag, add \(M_t=C_0(C)\) and the corresponding ordered inner-label
equalities to the adjacency condition (5.11).  The same Hall proof then
remains exact.  Those extra equalities are deliberately absent from the
fixed-annulus formulation, where all controlled depths begin at \(q_0\).

This is stronger than separate marginal balance.  Once the chronology
is fixed, the erosion word has no residual freedom to change a lower or
upper flag at an endpoint.

If the fixed SCD pairing is discarded and one asks only for some exact
two-sided annular symmetric-chain resolution, the condition can be written
as follows.  There must be nested endpoint sets

\[
   A_H\subseteq A_{H-1}\subseteq\cdots\subseteq A_{q_0}
   \tag{5.13}
\]

such that, for every \(q\), both restrictions

\[
   \Phi_q^-|_{A_q},\qquad \Phi_q^+|_{A_q}
   \tag{5.14}
\]

are bijections onto the two signed rank layers.  At one depth, make the
bipartite multigraph whose edge labelled \(t\) joins
\(\Phi_q^-(t)\) to \(\Phi_q^+(t)\).  A common \(A_q\) exists exactly when
this graph has a perfect matching.  Separate lower and upper image
fullness, or even separate lower and upper transversals, does not imply
this common matching.  Across depths, the nesting in (5.13) is an
additional integral condition.

For mere literal coverage, (5.13) is unnecessarily strong.  The scheduled
erosion intervals give the sufficient repair bill

\[
 \sum_{q=q_0}^{H}
 \left(
 N_q-|\operatorname{im}\Phi_q^-|
 +N_q-|\operatorname{im}\Phi_q^+|
 \right).
 \tag{5.15}
\]

A target absent from a scheduled image may still be represented by some
other interval of the same word.  Therefore (5.15) is exact for the
designated trace schedule and sufficient for unrestricted literal
coverage, but it is not a lower bound on every possible use of the word.

## 6. A sharp successor-edit stability lemma

The preceding Hall theorem explains exact annular compatibility.  The
next result quantifies how much of the unconditional shallow PBBS support
survives a common-chronology rewrite.

Let \(P\) and \(F\) be directed cycle factors on the same owner vertex
set.  Put

\[
   e=|E(P)\setminus E(F)|.
   \tag{6.1}
\]

Fix a sign and a depth \(q\).  Assume the reference factor \(P\) has one
correct \(q\)-edge trace for every target on that signed layer.

### Lemma 6.1 (support stability under successor edits)

The corresponding trace family of \(F\) misses at most

\[
   \boxed{qe}
   \tag{6.2}
\]

targets.

More generally, if the reference family already has \(d_q\) holes, the
new family has at most \(d_q+qe\) holes.

#### Proof

Choose one correct reference window for every target hit by \(P\).  For a
fixed sign, the chosen starts are distinct, because one start has one
trace value.  If every edge of a chosen \(q\)-edge \(P\)-window belongs
to \(F\), the indegree-one and outdegree-one conditions force those edges
to remain consecutive in \(F\), with the same owner sequence and hence
the same trace.

Every missing \(P\)-edge lies in at most \(q\) cyclic \(q\)-edge
windows.  Therefore at most \(qe\) chosen witnesses are spoiled.  Add
the pre-existing \(d_q\) holes for the general statement. \(\square\)

If an \(F\)-cycle is subsequently cut without a collar, each new cut edge
is charged in the same way.  With the standard \(2H\)-letter collars of
Theorem 5.1, no additional support loss occurs.

### Theorem 6.2 (even one-baseline hybrid owner ledger)

Let \(P\) be a reference factor whose two signed depth-\(q\) traces cover
every target for \(1\le q\le h<q_0\).  Let \(F\) be a cycle factor on the
same \(W\) owners satisfying the hypotheses of Theorem 5.1 through depth
\(H\), with \(C\) components.  Assume

1. the fixed-SCD Hall condition (5.12) holds, so every signed annular
   target at \(q_0\le q\le H\) is represented; and
2. the aggregate actual support deficit of \(F\) in the uncontrolled gap
   is

   \[
      \Gamma_{h,q_0}
      =\sum_{q=h+1}^{q_0-1}
       \left(N_q-|\operatorname{im}\Phi_q^-|
             +N_q-|\operatorname{im}\Phi_q^+|\right).
      \tag{6.3}
   \]

Then one literal word covers the middle layer and every signed depth
through \(H\), and has length at most

\[
   \boxed{
   W+2HC+h(h+1)e+\Gamma_{h,q_0}.}
   \tag{6.4}
\]

#### Proof

Use the erosion word and collars of Theorem 5.1.  It costs \(W+2HC\)
and covers every middle owner.  The fixed-SCD matching supplies every
annular target.  By Lemma 6.1, the two signs at depth \(q\le h\) have at
most \(2qe\) holes.  Summing gives

\[
   2e\sum_{q=1}^{h}q=h(h+1)e.
   \tag{6.5}
\]

Append those missing targets and the actual gap targets counted in
(6.3), one nonempty set-letter each.  This gives (6.4). \(\square\)

Thus this route needs

\[
   HC=o(W),\qquad h^2e=o(W),\qquad
   \Gamma_{h,q_0}=o(W).
   \tag{6.6}
\]

An unrelated annular path cover may have \(e=\Theta(W)\).  Common middle
ownership alone gives no edit bound.

## 7. Direct odd PBBS ledger

On \([2m+1]\), let the owners be rank-\(m\) sets.  The direct odd lower
depth-\(q\) trace uses \(q\) successor edges,

\[
   \Phi_{q}^{-,P}(X)=\bigcap_{i=0}^{q}P^iX,
   \tag{7.1}
\]

whereas the paired upper depth-\(q\) trace uses \(q+1\) edges,

\[
   \Phi_{q}^{+,P}(X)=\bigcup_{i=0}^{q+1}P^iX.
   \tag{7.2}
\]

The same proof as Lemma 6.1 gives respectively \(qe\) and \((q+1)e\)
holes.  Summing the lower depths \(1\le q\le h\) and the upper depths
\(0\le q\le h\) gives

\[
 e\sum_{q=1}^{h}q+e\sum_{q=0}^{h}(q+1)
 =(h+1)^2e.
 \tag{7.3}
\]

The direct odd delayed-atom compiler copies \(2H+1\) positions per
component.  Therefore, if an odd annular provider atlas has been aligned
to a full \(H\)-safe common owner factor \(F\), the exact analogue of
(6.4) is

\[
   \boxed{
   W_o+(2H+1)C+(h+1)^2e+\Gamma_{h,q_0}^{\rm odd}.}
   \tag{7.4}
\]

In particular, \(e=O(W_o/m)\) is strong enough for every
\(h=o(\sqrt m)\), while for one chosen growing \(h\) the weaker condition
\(e=o(W_o/h^2)\) suffices.

## 8. Adversarial audit and exact remaining boundary

The strongest claims above have the following limitations.

1. **The overlay no-go is template-specific.**  Theorem 1.2 refutes a
   common master word which preserves both designated middle-witness
   systems.  It does not refute a wholesale rewrite which abandons the
   partial compiler's singleton witnesses.  The morphological word does
   exactly that.

2. **The shallow endpoint bound is word-specific.**  Theorem 3.1 applies
   to the current partial-SCD word with its (W-N_{q_0}) literal
   rank-(m) repairs.  It is not a lower bound for every possible word
   built from the same abstract providers.

3. **Scheduled image holes are not universal holes.**  Formula (5.15)
   counts missing designated erosion traces.  Other intervals can only
   improve literal coverage.  Exact SCD ownership, in contrast, really
   does require a common nested assignment, and fixed-SCD ownership
   really does require (5.12).

4. **PBBS supplies only the shallow reference factor.**  The
   unconditional (h=o(\sqrt m)) compiler does not give an
   (H=A\sqrt m)-safe common factor.  Residences of lengths between
   (h) and (H), the associated cuts, and their crossing charts are not
   removed by the morphological identity.

5. **The current annular theorem is partial.**  It chronologizes only
   (N_{q_0}) providers and appends the other owners as singleton
   repairs.  It does not construct the full owner factor (F) required
   in Theorems 6.2 and 7.4, and it gives no estimate for
   (e=|E(P)\setminus E(F)|).

6. **There is an uncontrolled rank gap.**  A fixed entrance
   (q_0=a\sqrt m) and a PBBS band (h=o(\sqrt m)) leave all depths
   (h<q<q_0).  The exact bill is \(\Gamma_{h,q_0}\).  Neither input
   proves it is (o(W)).  Fixed-(a) diagonalization alone supplies no
   rate which closes this gap.

   The newer inner-flag-coherent SCD reduction is a genuine but different
   escape: it chooses \(q_0=o(m^{1/3})\), keeps the original SCD flags at
   every shallow depth, and appends exactly

   \[
      2\sum_{q<q_0}(N_q-N_{q_0})=o(W)
   \]

   shallow targets.  It therefore needs no PBBS word at all, conditional
   on its own bridge-one path-cover theorem.  It does not validate fusion
   at the fixed Gaussian entrance treated here.

7. **Parity has not been coupled.**  The partial-SCD notes are native on
   ([2m]), while the unconditional PBBS note is native on
   ([2m+1]).  The standard trimmed one-coordinate lift preserves
   coefficient asymptotics for separate words, but it is not a proved
   same-owner, same-successor lift satisfying (5.11).  Equation (7.4) is
   therefore a conditional direct-odd ledger, not an application of the
   existing even SCD scaffold.

8. **Collars must be paid at the two-sided rate.**  The lower
   morphological schedule alone needs only an (H)-prefix at a cut.
   Simultaneously preserving the upper windows uses intervals of length
   (2H+1), hence the (2H) term in (5.6), or (2H+1) in the direct odd
   compiler.  Replacing this by (HC) would be an undercount.

A clean surviving sufficient statement for the fixed-annulus/PBBS route
may therefore be written as follows.

> **PBBS-near fixed-SCD common-factor gate.**  On one common parity,
> construct a full owner-simple \(H\)-safe factor \(F\) such that
> \(HC=o(W)\), the compatibility graph (5.11) has a matching saturating
> all retained SCD providers, \(e=o(W/h^2)\) relative to the PBBS
> reference factor, and \(\Gamma_{h,q_0}=o(W)\).

Under that statement, Theorem 6.2 or 7.4 gives a literal hybrid with one
middle baseline.  None of its four quantitative clauses follows from the
current fixed-annulus partial-SCD theorem.  Hence the audited conclusion
is

\[
 \boxed{
 \begin{gathered}
 \text{direct or sparse fusion of the existing words is rigorously
 impossible;}\\
 \text{wholesale one-baseline fusion is conditionally exact but remains
 unproved.}
 \end{gathered}}
 \tag{8.1}
\]
