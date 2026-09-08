# The zero-orbit bridge cannot be locally transplanted into d80

Date: 2026-07-29

Status: proved an exact three-owner port obstruction, a residence-transversal
lower bound, and an exact common-compiler collar criterion. The literal
three-action bridge is not transplantable into the distance-80 factor. A
jointly resident and compilable replacement is not constructed.

## 1. The three objects must not be conflated

The authoritative Hall-19 middle chronology (and its abstract compiler
graph) is

    scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
    SHA-256 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b

Its six degree-zero compiler targets lie in the six distinct rotation
orbits

\[
 4821,\quad 851,\quad 3405,\quad 2709,\quad 2473,\quad 1861.
\tag{1.1}
\]

The exact d93 three-action bridge is stored in

    scratch/k15_zero_orbit_full_k3.result.json
    SHA-256 42be4bc5ccb87bd550c5cc7888a19e398ca1bdcd5852cba8a3e7f4e89c09a1a8

and audited in
MATH_CERTIFICATE_K15_H19_ZERO_ORBIT_THREE_ACTION_BRIDGE_20260729.md.
It is a quotient-factor certificate, not a compiler word.

The distance-80 factor is

    scratch/k15_resident_q1factor_d80_snapshot.json
    SHA-256 bc734aa673ce1efc7b72e298c5765e526daee87c948ccc9a4db947d7313cd557

The adjective “resident” in its filename means resident-centred. The factor
itself is not depth-three resident: it has 240 positive runs of length two
and 435 of length three. By the exact erosion criterion, it is not \(D^3A\)
for any nonempty source word \(A\). Consequently no physical common
compiler is presently attached to d80.

Its four relevant physical lower-\(q=2\) loads are

\[
 (\lambda_{851},\lambda_{1861},\lambda_{2473},\lambda_{2709})
   =(15,15,45,0).
\tag{1.2}
\]

Thus d80 already supplies the \(1861\) orbit repaired by the d93 bridge. Its
missing zero-orbit resource is \(2709\). This face mismatch is independent
of Hall matching.

## 2. Closed-current, residence, and compiler conditions

For a quotient choice \(c=(L,a,b)\), put

\[
 p(c)=e_{[L\cup\{a\}]}+e_{[L\cup\{b\}]},
 \qquad
 \kappa(c)=[L\cup\{a,b\}],
\tag{2.1}
\]

where brackets denote the fixed cyclic-orbit representative/index. If a
base selector uses \(c_L\) and a terminal selector uses \(c'_L\), define

\[
 \partial K=\sum_{L\in K}\bigl(p(c'_L)-p(c_L)\bigr).
\tag{2.2}
\]

### Lemma 2.1 (closed-current collared selector transplant)

Work at \(k=15\) with the \(C_{15}\)-equivariant catalogue; every rank-seven
owner orbit and rank-eight endpoint orbit is full. Let \(F\) be an
equivariant Johnson two-factor and change exactly the owner orbits in \(K\).
Write \(\bar\lambda_9(U)\) for the number of selected quotient
choice-orbits having upper colour \(U\); this is not a physical phase load
when \(U\) is a short orbit. On each oriented terminal component define

\[
 T'_{i+1}=T'_i-\{\alpha'_i\}+\{\beta'_i\},
\]

with indices taken cyclically within that component. The following are
necessary for a residence-safe, upper-\(q=1\)-complete terminal factor:

1. \(\partial K=0\);
2. for every rank-nine orbit \(U\),

   \[
    \bar\lambda'_9(U)=\bar\lambda_9(U)
      -\#\{L\in K:\kappa(c_L)=U\}
      +\#\{L\in K:\kappa(c'_L)=U\}>0;
   \tag{2.3}
   \]

3. the removed old physical edges hit the closed span of every old positive
   run of length at most three; and
4. every newly formed seam collar satisfies

   \[
    \beta'_i\ne\alpha'_{i+t},
    \qquad t=1,2,3,
   \tag{2.4}
   \]

   whenever the corresponding edge interval meets a changed seam.

In the cut-and-rejoin retained-segment class, if every retained segment has
at least four carrier vertices, conditions 3–4 are also sufficient for
residence. Without this separation, the equivalent replacement is the
state-expanded collar test retaining the last four carrier states.

#### Proof

The base has degree two. Its terminal degree vector is the base vector plus
\(\partial K\), proving condition 1. Equation (2.3) is the literal signed
choice-colour ledger. If an old bad run has no removed edge in its closed
span, that entire zero–positive–zero segment remains in the terminal
two-factor and the defect persists. This proves condition 3. Every new
short run must meet a changed seam, and its entering and leaving labels are
equal exactly when (2.4) fails. Under separation no run of length at most
three meets two seams, giving sufficiency. The state-expanded statement is
the same test with the whole incoming history retained. \(\square\)

The next theorem is the compiler condition missing from a Hall-only
argument.

### Theorem 2.2 (exact fixed-injection common-compiler transplant)

Let \(T'=(T'_0,\ldots,T'_{W-1})\) be a fixed linear resident physical
chronology. Let \(\Gamma\) be a finite injection of required lower targets
into distinct cells \((t,i)\), where \(0\le t\le2\) and
\(0\le i\le W+2-t\). In the \(k=15,d=3,r=8\) compiler application the
injection is graded, so a target assigned to row \(t\) has
\(|S|=5+t\). Form the pin family

\[
 \mathcal P_\Gamma=
 \{(3,i,T'_i):0\le i<W\}
 \cup\{(t,i,S):(S,(t,i))\in\Gamma\}.
\tag{2.5}
\]

Any source positions required to retain an old compiler letter are included
as singleton pins \((0,p,A^{\rm old}_p)\). For each coordinate
\(x\in[15]\), put, using integer position intervals,

\[
 Q_x=[0,W+2]\setminus
 \bigcup_{\substack{(t,i,S)\in\mathcal P_\Gamma\\x\notin S}}[i,i+t].
\tag{2.6}
\]

There exists one word \(A'\), every letter of which is nonempty, realizing
every pin in \(\mathcal P_\Gamma\) if and only if

\[
 x\in S\Longrightarrow Q_x\cap[i,i+t]\ne\varnothing
 \quad\text{for every }(t,i,S)\in\mathcal P_\Gamma,
\tag{2.7}
\]

and

\[
 \bigcup_xQ_x=[0,W+2].
\tag{2.8}
\]

When these conditions hold, the maximal word

\[
 A'_p=\{x:p\in Q_x\}
\tag{2.9}
\]

is such a common compiler. Hence a proposed target-to-cell injection
\(\Gamma\) is jointly realizable precisely when (2.7)–(2.8) hold. An
abstract matching can be lifted precisely when its physical cells can be
chosen to form such an injection; the conditions depend on the whole pin
family, not on its edges separately.

#### Proof

If \(x\notin S\), every position of \([i,i+t]\) is deleted from \(Q_x\), so
the interval union in (2.9) contains no forbidden coordinate. If \(x\in S\),
(2.7) supplies \(x\) somewhere in that interval. Thus every pin union is
exactly \(S\). Equation (2.8) makes every source letter nonempty. This proves
sufficiency.

Conversely, in any realizing word, a coordinate forbidden by some pin cannot
occur at any position removed in (2.6); its support is contained in \(Q_x\).
Every required coordinate must therefore satisfy (2.7), and nonempty source
letters force (2.8). \(\square\)

If altered source collars are disjoint and no pin interval meets two of
them, Theorem 2.2 factors collarwise after the transported outside singleton
pins are fixed. This is the exact collar-transplant lemma. It includes
negative coordinate exclusions and source nonemptiness; ordinary Hall does
not.

## 3. What the d93 bridge actually proves

Relative to d93, the three changes are one-end endpoint currents

\[
 392\longrightarrow96,\qquad
 96\longrightarrow349,\qquad
 349\longrightarrow392.
\tag{3.1}
\]

They form a closed current, preserve degree two, and delete only duplicated
upper-\(q=1\) colours. The terminal quotient cycles have

\[
 (\text{length},\text{voltage})=(360,\pm4),(69,\pm1),
\tag{3.2}
\]

and lift to physical cycles of lengths \(5400,1035\).

The factor is not residence-safe. All 1,050 old d93 defects persist, and the
bridge creates one additional rotation orbit of fifteen length-three
defects, for

\[
 570+495=1065
\tag{3.3}
\]

total defects. The new orbit is created in the collar of
\((1837,6,13)\). The bridge also is not shadow-neutral beyond \(q=1\): it
repairs lower-\(q=2\) orbits \(1861,4757\), loses \(1325\), repairs
lower-\(q=3\) orbits \(557,1349\), and leaves the seventeen unrestricted
upper holes unchanged.

Therefore the certificate is an exact marginal circulation primitive, not
a resident or common-compiler construction.

## 4. Exact failure of the literal transplant into d80

The d80 choices at the three bridge owners differ from d93 at two owners.
Their port ledger is

\[
\begin{array}{c|c|c|c}
L&\text{d80 old choice/ports}&\text{bridge new choice/ports}&\Delta_L\\ \hline
1837&(12,13):(392,395)&(6,13):(96,395)&e_{96}-e_{392}\\
1893&(1,14):(94,276)&(12,14):(349,276)&e_{349}-e_{94}\\
4759&(3,5):(307,309)&(10,11):(392,404)
 &e_{392}+e_{404}-e_{307}-e_{309}.
\end{array}
\tag{4.1}
\]

Consequently

\[
 \partial K=e_{96}+e_{349}+e_{404}
             -e_{94}-e_{307}-e_{309}\ne0.
\tag{4.2}
\]

The proposed selector has degree three at \(96,349,404\) and degree one at
\(94,307,309\). It is not a two-factor.

This is not an upper-\(q=1\) failure. Its signed colour ledger is

\[
 -5815-3791-4799+7605+5819+5949,
\tag{4.3}
\]

and the three deleted colours have d80 loads \(3,2,2\).

### Theorem 4.1 (three-owner rigidity on d80)

Holding every other d80 owner fixed, the original choices at
\(1837,1893,4759\) are the only degree-balanced selection on these three
owners. In particular, no nontrivial three-owner transplant of the bridge
exists.

#### Proof

For a one-end realization of the current triangle (3.1), the complete old
socket table is

\[
\begin{array}{c|c|c}
\text{desired current}&\text{old d80 socket}&
  \text{replacement with the same pivot}\\ \hline
392\to96&(1837;395)&\text{yes}\\
392\to96&(5421;394)&\text{no}\\
96\to349&(877;179)&\text{no}\\
96\to349&(1645;262)&\text{no}\\
349\to392&(1497;190)&\text{no}\\
349\to392&(2653;405)&\text{no}.
\end{array}
\tag{4.4}
\]

Thus only the first side of the current triangle has a d80 socket.

For the stronger fixed-owner statement, endpoint balance requires the new
six-port multiset to equal the old six-port multiset. A port outside the old
multiset has no negative occurrence and cannot cancel. The complete choices
at each fixed owner whose two ports lie in the old multiset are

\[
\begin{array}{c|l}
1837&(12,13):(392,395)\\
1893&(1,14):(94,276)\\
4759&(3,5):(307,309),\ (3,10):(307,392),
       \quad(5,10):(309,392)\\
\end{array}
\tag{4.5}
\]

The first two owners are forced. They consume ports
\(392,395,94,276\), leaving \(307,309\); hence the third owner is forced to
\((4759,3,5)\). These are exactly the original d80 choices. \(\square\)

## 5. Residence makes every three-action repair impossible

### Lemma 5.1 (nine-span bound per physical edge)

In a rank-eight Johnson factor, one physical edge belongs to the closed
spans of bad positive runs for at most nine coordinates.

#### Proof

If an edge \(XY\) lies in the entering, internal, or leaving part of the
positive run of coordinate \(x\), then \(x\in X\cup Y\). A Johnson edge has

\[
 |X\cup Y|=9.
\]

For a fixed coordinate, positive-run spans are disjoint at that edge.
Therefore at most nine bad-run spans contain it. \(\square\)

### Corollary 5.2 (five owner orbits are necessary)

Every residence-clean equivariant selector obtained from d80 changes at
least five lower-owner choices.

#### Proof

Every one of the 675 old bad-run spans must contain a removed old edge by
Lemma 2.1. One changed owner removes fifteen rotated physical edges, and by
Lemma 5.1 these hit at most \(15\cdot9=135\) bad spans. Hence

\[
 |K|\ge\left\lceil{675\over135}\right\rceil=5.
\]

\(\square\)

Thus no three-action packet, whether or not it is the d93 packet, can turn
d80 into a resident selector.

### Proposition 5.3 (literal bridge support forces 35 owner changes)

Every residence-clean \(C_{15}\)-equivariant selector containing the three
literal d93 bridge choices at owners \(1837,1893,4759\) differs from d80 at
at least \(35\) owner orbits.

#### Certificate proof

For the literal bridge support there is a much stronger certificate-audited
bound. Its 45 forced old physical edges hit only thirty of the 675 bad-run
spans. With those cuts fixed, the exact residual circular-interval
instances are

\[
\begin{array}{c|c|c}
\text{component length}&\text{remaining bad-run spans}&
  \text{minimum additional old edges}\\ \hline
3615&270&210\\
1050&120&90\\
1050&150&105\\
720&105&75
\end{array}
\tag{5.1}
\]

and therefore require \(480\) additional old edges in total. Hence
every equivariant residence-clean extension containing the literal bridge
support changes at least

\[
 {45+480\over15}=35
\tag{5.2}
\]

owner orbits. This is a necessary old-defect bound; inserted-edge collars
may force more.

The span extractor is
scratch/audit_k15_phasefactor_safe_openings.py (SHA-256
cf1e33cb0d592be6b55955538a4904eb0949600a9dbb7a884524e99409e10366),
and the exact circular-interval stabber is
scratch/audit_k15_factor_min_residence_cuts.py (SHA-256
d326c1212d90d2848b6e00947679033529395716c320325263d3b97a65693179).
The latter tries every pivot in one circular interval and then applies the
right-end greedy theorem to the resulting linear interval family. No
separate JSON for the forced-45 recomputation is stored.

\(\square\)

## 6. The correct d80 service target is 2709

The d93 \(2709\) witness uses choices

\[
 (3733,8,14),\qquad(5419,6,11).
\tag{6.1}
\]

d80 already contains the helper \((5419,6,11)\), but at owner \(3733\) it
uses \((3733,1,13)\). The canonical service action is therefore

\[
 (3733,1,13)\longrightarrow(3733,8,14).
\tag{6.2}
\]

Its old and new endpoint pairs are

\[
 (267,367)\longrightarrow(297,375),
\tag{6.3}
\]

and its upper colour changes from \(5981\) to \(5535\). Colour \(5981\) has
d80 load one, so any \(q=1\)-complete packet containing (6.2) must recreate
\(5981\) elsewhere.

### Proposition 6.1 (the canonical service needs four owner changes)

Every endpoint-balanced d80 replacement packet containing (6.2) changes at
least four owner orbits. In particular, there is no degree-balanced
three-action packet containing (6.2).

#### Proof

First, two compensating actions are necessary: they must remove the positive
endpoints \(297\) and \(375\). The selected d80 sockets at those vertices are

\[
\begin{array}{c|c}
297&(1311;49),(2965;186)\\
375&(4787;310),(5419;369).
\end{array}
\tag{6.4}
\]

No old selected edge contains both \(297\) and \(375\), so one owner must be
chosen from each row. For each of the four owner pairs, the exact number of
replacement pairs whose endpoint current is the inverse of (6.3) is

\[
\begin{array}{c|cc}
 &4787&5419\\ \hline
1311&0&0\\
2965&0&0.
\end{array}
\tag{6.5}
\]

This is a complete local catalogue check, not a global search. Thus two
auxiliary actions cannot close the current, proving the four-owner lower
bound. \(\square\)

The canonical \(2709\) service action therefore needs at least three
auxiliary owner changes for degree balance, and possibly more for colour
\(5981\), residence, shadows, and compilation.

Combining (6.5) with Corollary 5.2, five changed owners are the first
possible shell for any residence-clean d80 repair, but feasibility at five
is unproved.

## 7. Exact residual construction gate

A jointly realizable d80 improvement must now satisfy all of the following
in one terminal object:

1. choose a packet \(K\) of owner replacements with \(\partial K=0\);
2. preserve every upper-\(q=1\) colour by (2.3), including any unique colour
   removed by a \(2709\)-service action;
3. hit all 675 old bad-run spans and pass every new joint collar test
   (2.4);
4. contain an actual physical \(2709\) lower-\(q=2\) witness, rather than a
   redundant second \(1861\) witness;
5. preserve or repair all other lower and upper shadow targets;
6. choose the required physical topology and unfold one chronology;
7. choose distinct physical compiler cells for at least \(16{,}365\)
   distinct lower targets (and ultimately for all \(16{,}383\)); and
8. pass the common-word conditions (2.7)–(2.8), including every middle pin.

Items 7–8 are the jointly realizable compiler condition. A quotient orbit
load or an abstract Hall-rank increase does not imply them.

The first concrete improvement target is therefore one physical triple

\[
 (T',A',M')
\tag{7.1}
\]

for which \(T'=D^3A'\) is residence/shadow valid, every selected matching
edge of \(M'\) is a literal cell of the one common word \(A'\), and

\[
 |M'|\ge16365.
\tag{7.2}
\]

The authoritative Hall-19 abstract graph has matching number \(16364\).
Thus (7.2) is a jointly realized partial matching of deficiency at most
eighteen and is a genuine compiler improvement; merely giving one of its
zero targets a positive quotient-shadow load is not. Full lower compilation
would require \(|M'|=16383\).

The literal three-owner d93 transplant is therefore ruled out on d80. The
same three choices are not ruled out as part of a larger packet; forcing
their exact support in a residence-clean equivariant selector requires at
least \(35\) owner changes. Their surviving role is as a template for a
larger endpoint-balanced packet. The first possible owner-count shell for a
different residence-clean repair is five, but this is only a necessary
lower bound, not a sufficient formulation. The smallest unproved
replacement statement at that shell is:

> **Unproved five-or-more-owner packet lemma.** There exists an
> endpoint-balanced, \(q=1\)-complete replacement packet relative to d80
> whose old-edge support hits every bad-run span, whose inserted collars are
> residence-safe, whose terminal factor supplies \(2709\) and all remaining
> shadows, and whose unfolded physical pins satisfy Theorem 2.2 for an
> appropriately graded injection \(\Gamma\) of at least \(16{,}365\)
> distinct lower targets.

No part of this note assumes that lemma, and no Hall-18 common-word
improvement or coefficient-one conclusion follows without it.

## 8. Adversarial scope audit

* The d80 object is not resident. “Transplanting its compiler” is therefore
  meaningless until a residence-clean terminal chronology exists.
* The d93 bridge is degree-balanced only relative to d93. Endpoint current
  is base-dependent.
* The d80 missing special orbit is \(2709\), not \(1861\).
* Equations (5.1)–(5.2) are a certificate-audited finite strengthening;
  the hand proof of Corollary 5.2 is independent of that census. The
  resulting \(35\) is a necessary selector-Hamming bound only when the
  literal three bridge choices are forced; it is neither sufficient nor a
  bound for phase-specific cut/seam surgery or homologous packets on other
  owners.
* A raw lower-shadow witness is not a compiler cell until residence,
  chronology, a distinct cell assignment, and all PCSH exclusions are
  simultaneously fixed.
* The common-compiler theorem is necessary and sufficient only for a fixed
  physical chronology and fixed target-to-cell injection. Finding those
  objects remains part of the residual gate.
