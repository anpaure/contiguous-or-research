# Candidate 0575, the duplicate-child splitter, and the repeated-axis comparison

Date: 2026-07-28

Status: exact interpretation of the provisional Hall-20 descent; proved
fixed-basis splitter theorem; proved same-axis simultaneous-shrink lemma; exact
comparison with the two axis-13 `2/1` circuits; and an H100-audited one-braid
no-go for the stronger native-ear normal form at the canonical Hall-21 state.
This note itself does not claim a Hall-19 carrier, a discharge of a
degree-zero target, or a global 16,363-pin common-word lift.  A separate,
subsequently audited profile-router route has advanced the global frontier to
Hall 19; it is recorded below only to prevent this scoped analysis from being
mistaken for the current global frontier.

All coordinate numbers are zero based unless explicitly called one based.
Put

\[
 k=15,\qquad r=8,\qquad d=3,\qquad
 W=\binom{15}{8}=6435,
 \qquad N=\sum_{j=1}^{7}\binom{15}{j}=16383.
\]

## 1. Terminology correction and the exact route

The label `c0575` is a census index, not physical cell 575 and not the
improving braid.  Among the 687 nonidentity Hall-21-neutral braid endpoints,
candidate 0575 is the unique endpoint whose canonical positive DM shore has
left size 702.  It is produced by

\[
 \operatorname{RF}(1510,5017,6136).
\]

The improving splitter *from* candidate 0575 is

\[
 \operatorname{RF}(885,1393,3668).
\]

Thus the exact route is

\[
 H21/z6\xrightarrow{\operatorname{RF}(1510,5017,6136)}
 H21^{\rm comp}/z6
 \xrightarrow{\operatorname{RF}(885,1393,3668)}H20/z6.       \tag{1.1}
\]

The frozen carriers and hashes are

```text
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
  scratch/k15_segment_braid_hall21_zero6.json
ea5259c4bb8a15444da135f7c6369e11fbc059f322c570fd3db2e6b8509af337
  scratch/k15_segment_braid_hall21_compressed_dm702.json
9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
  scratch/k15_segment_braid_hall20_zero6.json
```

Their matching ranks, deficiencies, and canonical DM shores are

\[
\begin{array}{c|ccc}
 &H21&H21^{\rm comp}&H20\\ \hline
\nu&16362&16362&16363\\
N-\nu&21&21&20\\
|S|/|N(S)|&846/825&702/681&677/657.
\end{array}                                                     \tag{1.2}
\]

Every carrier is an exact permutation of the 6435 middle masks, is a Johnson
path, is depth-three resident, and has complete upper support at every depth.
The lower-hole vectors are

\[
 (4,18,9,1,0,0,0),\quad
 (4,18,11,1,0,0,0),\quad
 (4,18,11,1,0,0,0).                                           \tag{1.3}
\]

In particular, the neutral router loses lower depth-three targets 1801 and
5000.  The six degree-zero targets remain exactly

\[
 \{5801,13616,13620,17738,21641,29776\}.                       \tag{1.4}
\]

## 2. Which component and which axes are actually discharged

The neutral router removes the `169/168` positive-DM component rooted at
1920 and creates a `25/24` component rooted at

\[
                              \rho=1801.                        \tag{2.1}
\]

The new target set is

\[
\begin{split}
C=\{&1801,1803,1805,1807,1833,1835,1837,1865,1867,1869,1897,
1933,1993,\\
&5897,5899,5961,9993,9997,10025,14089,18185,18187,18249,22281,
26377\}.
\end{split}                                                     \tag{2.2}
\]

It has target-rank histogram `(1,7,17)` in ranks `(5,6,7)`.  Its 24
right cells have pairwise distinct native traces equal to
`C minus {1801}`.  Hence it is a rooted native-basis circuit.

The improving braid acts on the Boolean square

\[
 \alpha=1,\qquad \beta=5,
\]

\[
 Q=\{\rho,\rho+2^\alpha,\rho+2^\beta,
             \rho+2^\alpha+2^\beta\}
   =\{1801,1803,1833,1835\}.                                  \tag{2.3}
\]

It partitions this square into the two parallel `beta`-fibres

\[
 Q_0=\{1801,1833\},\qquad Q_1=\{1803,1835\},                  \tag{2.4}
\]

and its exact net restricted-profile identity is

\[
                         Q\longmapsto Q_0\sqcup Q_1.           \tag{2.5}
\]

Thus coordinate `alpha=1` is the fibre-separation coordinate and
`beta=5` is the coordinate along each retained edge.  In one-based
notation these are coordinates 2 and 6.  The successful splitter does not
discharge either repeated axis-13 component.

The relevant physical rows are

\[
\begin{array}{c|c|c|c|c}
\text{state}&\text{cell}&\text{depth/start}&P\text{-tuple}&
 \Gamma_C\\ \hline
H21^{\rm comp}&8097&1/1659&(809,1577)&Q_0\\
H21^{\rm comp}&14269&2/1394&(810,1578,1067)&Q\\
H20&9334&1/2896&(1577,809)&Q_0\\
H20&9599&1/3161&(1577,809)&Q_0\\
H20&16035&2/3160&(1067,1577,809)&Q_1.
\end{array}                                                     \tag{2.6}
\]

One `Q_0` copy cancels between the profile multisets.  The remaining 23
common component profiles have rank 23 and match

\[
                              C\setminus\{1801,1835\}.          \tag{2.7}
\]

The old `Q` cell can serve 1835, giving local rank 24.  At the final endpoint,
the new `Q_0` cell serves 1801 and the `Q_1` cell serves 1835, giving local
rank 25.

There is also an exact cut formula.  For every target subset (A\subseteq C),
replacing one `Q` cell by cells `Q_0,Q_1` changes its neighbourhood size by

\[
\begin{split}
\Delta |N(A)|
 &=\mathbf 1[A\cap Q_0\ne\varnothing]
   +\mathbf 1[A\cap Q_1\ne\varnothing]
   -\mathbf 1[A\cap Q\ne\varnothing]\\
 &=\mathbf 1[A\cap Q_0\ne\varnothing\ \text{and}\
              A\cap Q_1\ne\varnothing].                      \tag{2.8}
\end{split}
\]

Every cut meeting only one fibre is unchanged; every cut meeting both fibres
gains exactly one neighbour.  Equation (2.7) then supplies an explicit
perfect matching, so (2.8) is not being used as a marginal proxy.

### Independent exterior-rank audit

Delete the 25 targets (C) and their complete 25-cell final neighbourhood.
A maximum matching of size 16363 loses at most 25 edges, so the residual
rank is at least 16338.  The final `677/657` DM shore is target- and
right-disjoint from this deleted block and remains a gap-20 shore in the
residual target universe of size (16383-25=16358).  Hall's theorem gives
the reverse bound

\[
                        \nu_{\rm ext}\le 16358-20=16338.
\]

Therefore

\[
 \nu_{\rm ext}=16338,
 \qquad 24+16338=16362,
 \qquad 25+16338=16363.                                      \tag{2.9}
\]

This component decomposition is distinct from the full-profile contraction
audit.  Cancelling all 19,311 occurrence profiles gives common rank 16345
and boundary ranks (17\to18).  Confusing 16338 with 16345 would mix a
component deletion with a full collar contraction.

## 3. Exact fixed-basis splitter theorem

The preceding mechanism has a smaller exact abstraction than a native-root
ear.

### Theorem 3.1 (two-provider completion of a rooted basis)

Let (G_0=(L,R_0;E_0)) be a finite bipartite graph with matching rank
(n=N-h).  Let (C\subseteq L) have (c\) targets and a target-labelled
basis

\[
                    \{b_x:x\in C\setminus\{\rho\}\},          \tag{3.1}
\]

where the (c-1) cells are distinct and (b_x\sim x).  Fix
(t\in C\setminus\{\rho\}).

Let (G_1) be another occurrence-labelled graph on the same target set.
Assume that (G_1) contains:

1. distinct target-labelled providers (b'_x\sim x) for every
   (x\in C\setminus\{\rho,t\});
2. two further distinct cells (u,v), disjoint from those (c-2) cells,
   such that the bipartite graph between
   ({\rho,t\}) and ({u,v}) has a perfect matching; and
3. a matching (M_{\rm ext}) of size (n-(c-1)) whose target endpoints
   avoid (C) and whose cell endpoints avoid all (c) local cells.

Then

\[
                              \nu(G_1)\ge n+1.                  \tag{3.2}
\]

Within this fixed target-labelled normal form, condition 2 is necessary and
sufficient for the local (c)-cell bank to saturate (C).  If (G_1) also
has a Hall shore of gap (h-1), then its deficiency is exactly (h-1).

#### Proof

The fixed bank in condition 1 matches (C\setminus\{\rho,t\}).  A perfect
matching in the displayed `2 x 2` graph covers the two exposed targets with
(u,v).  These (c) edges and (M_{\rm ext}) are target- and cell-disjoint,
so their union has size

\[
                         c+n-(c-1)=n+1.
\]

Conversely, once the (c-2) target-labelled providers are fixed, only
(u,v) can cover the two exposed targets.  The local bank saturates (C)
exactly when those two cells have a perfect matching to them.

Finally, (3.2) gives deficiency at most (h-1), while a gap-((h-1)) Hall
shore gives deficiency at least (h-1).  Hence equality holds. 
\(\square\)

The theorem permits the old (b_t) to disappear or merely go unused.  It
does not claim necessity for an arbitrary endpoint which reroutes the whole
basis.  The exterior-target disjointness is essential; cell disjointness
alone does not make the union a matching.

### Corollary 3.2 (Boolean fibre splitter)

Suppose, after cancelling common component profiles with multiplicity, the
old residual bank consists of one cell with shore
(Q=Q_0\dot\cup Q_1), and the new residual bank consists of two cells with
shores (Q_0,Q_1).  If a common target-labelled bank covers all but two
targets (ho\in Q_0) and (t\in Q_1), then the old local rank is one less
than the new local rank.  With the exterior and Hall-shore hypotheses of
Theorem 3.1, this is an exact unit deficiency descent.

#### Proof

The common bank leaves (ho,t) exposed.  One old cell can cover only one
of them; the two new cells cover both.  Equivalently apply Theorem 3.1, or
use the exact cut identity (2.8). 
\(\square\)

The root-1801 instance is Corollary 3.2 with

\[
   (\rho,t,Q_0,Q_1)
   =(1801,1835,\{1801,1833\},\{1803,1835\}).                  \tag{3.3}
\]

## 4. Literal duplicate-child tier

The graph theorem does not yet put the selected edges into one physical
word.  The successful endpoint has an additional structure: it duplicates a
native child and then shrinks one copy to the missing root.

### Theorem 4.1 (literal two-provider splitter)

In the setting of Theorem 3.1, let (P=(P_p)) be one nonzero word which
realizes the protected central windows and a selected family of native pins.
Assume:

1. every retained (b'_x\mapsto x), the cell (v\mapsto t), and the
   exterior pins claimed to be literal are either native under this same
   (P) or are included explicitly in the protected pin ledger;
2. cell (u), on interval (I), has native trace
   (s=\bigcup_{p\in I}P_p\supsetneq\rho), and (u\sim\rho);
3. a distinct cell (w\ne u) remains available for target (s) (when
   (s=t), this cell may be (v)); and
4. writing (D=s\setminus\rho), one has

   \[
       P_p\cap\rho\ne\varnothing\qquad(p\in I),               \tag{4.1}
   \]

   and, for every protected pin ((J,S_J)) and every
   (x\in D\cap S_J),

   \[
       \exists p\in J\setminus I\quad x\in P_p.               \tag{4.2}
   \]

Define

\[
 A_p=\begin{cases}
       P_p\cap\rho,&p\in I,\\
       P_p,&p\notin I.
     \end{cases}                                                \tag{4.3}
\]

Then the one word (A) realizes (u\mapsto\rho), all retained local
target pins, and every protected exterior pin.  In particular it literally
saturates (C).  Conditions (4.1)--(4.2) are necessary and sufficient for
this fixed one-interval shrink.

#### Proof

Because every (P_p) on (I) is a subset of the native trace (s),

\[
 \bigcup_{p\in I}(P_p\cap\rho)
   =\left(\bigcup_{p\in I}P_p\right)\cap\rho
   =s\cap\rho=\rho.                                           \tag{4.4}
\]

Condition (4.1) is exactly nonemptiness on the edited positions.  Only the
coordinates in (D) are deleted, and every occurrence of such a coordinate
inside (I) is deleted.  A protected pin retains that coordinate exactly
when (4.2) holds.  All other coordinates are unchanged.  Thus (4.1)--(4.2)
are sufficient.  Their failure respectively empties a letter or destroys a
required coordinate from a protected union, proving necessity.  The distinct
provider (w) keeps target (s) covered after (u) is reassigned.
\(\square\)

A graph-theoretic exterior matching satisfies the literal conclusion only
if all of its pins are included in the same survival ledger.  This is the
precise gap between local common-`Q` and a global common-word compiler.

### Theorem 4.2 (simultaneous common-axis shrink)

Let (e) be one coordinate and let (I_1,\ldots,I_q) be pairwise disjoint
native intervals of one word (P), with

\[
 \tau_P(I_i)=U_i=R_i\cup\{e\},\qquad e\notin R_i.              \tag{4.5}
\]

For every (i), retain a second physical provider for (U_i).  Put

\[
 I=\bigcup_{i=1}^q I_i,
 \qquad
 A_p=\begin{cases}P_p\setminus\{e\},&p\in I,\\P_p,&p\notin I.
 \end{cases}                                                    \tag{4.6}
\]

Then (A) realizes every exceptional root pin (I_i\mapsto R_i) together
with a protected native pin family if and only if

\[
 P_p\setminus\{e\}\ne\varnothing\quad(p\in I),               \tag{4.7}
\]

and every protected pin ((J,S_J)) with (e\in S_J) has an occurrence

\[
                 \exists p\in J\setminus I\quad e\in P_p.     \tag{4.8}
\]

#### Proof

On (I_i), deletion of (e) changes the native union (U_i) to (R_i).
It changes no other coordinate.  Conditions (4.7) and (4.8) are respectively
the exact point-nonemptiness and protected-union survival conditions.  The
same necessity argument as in Theorem 4.1 applies. 
\(\square\)

The shared coordinate reduces the literal survival audit to one deletion
mask, but it does not reduce matching capacity.  Covering (q) disjoint
`2/1` components requires (2q) distinct cells for their (2q) distinct
targets.  Starting from one child provider per component, at least (q)
additional or repurposed providers are necessary.

## 5. Exact literal realization of the root-1801 unit

For the final H20 controller, take

\[
 \rho=1801,\qquad t=1835,\qquad s=1833=1801\cup\{2^5\}.        \tag{5.1}
\]

Choose the common 23 native providers for (C\setminus\{1801,1835\}),
retain cell 9334 for (s=1833), use cell 16035 for (t=1835), and repin
cell 9599 from 1833 to 1801.  On positions 3161,3162 the maximal controller
pair is

\[
                         (1577,809).
\]

Delete bit (2^5=32):

\[
                         (1577,809)\longmapsto(1545,777).       \tag{5.2}
\]

The focal unions are exact:

\[
 1545\vee777=1801,
 \qquad
 1067\vee1545\vee777=1835.                                   \tag{5.3}
\]

The bit-5 controller run is positions 3159 through 3163.  Every affected
four-window therefore retains bit 5 at position 3159, 3160, or 3163.  The
only other retained focal interval meeting the edited pair is cell 16035,
which retains bit 5 at (P_{3160}=1067).  No interval among the 657 final-DM
native pins meets positions 3161 or 3162.  The complete certificate checks
3720 instances of the survival condition.

Consequently one word realizes

\[
                     25+657=682                               \tag{5.4}
\]

pairwise target- and cell-distinct pins: all 25 targets of the discharged
component and all 657 targets on the final critical shore.  The alternative
choice repins cell 9334 and retains cell 9599; it is equally valid.

This is literal thinning (A_p\subseteq P_p) beneath the final maximal
controller.  It does not make 1801 a native depth-zero trace.  Native grade
and maximal-controller congruence are bypassed by the common-`Q` shrink, not
violated.

The full matching rank 16363 follows from (2.9).  An exterior matching of
size 16338 exists, and 657 of the displayed literal pins lie in that exterior
target block, but no entire 16338-edge exterior matching has been realized in
this same word.  Extending the 682-pin certificate to a full matching would
require 15681 further simultaneous pins.

## 6. Seam and controller current: what is and is not invariant

Both braids in (1.1) are `RF`, namely

\[
 A|B|C|D\longmapsto A|\overleftarrow C|B|D.
\]

Their deleted and inserted seam-colour multisets agree exactly.  In
one-based coordinates they are

\[
\begin{array}{c|c}
\text{router}&\{\{8,15\},\{1,15\},\{7,15\}\}\\
\text{splitter}&\{\{8,12\},\{1,8\},\{2,8\}\}.
\end{array}                                                     \tag{6.1}
\]

Thus both turn-colour currents are zero.  The splitter's local fibre axis 5
(one-based coordinate 6) does not appear in its seam current.  A target
optional axis therefore need not be visible at a seam; the decisive change
may occur in an internally transported collar.

For the splitter, the noncommon maximal-controller letters satisfy

\[
 \{17449,16937,810,1578\}
 \longmapsto
 \{17450,16938,809,1577\}.                                    \tag{6.2}
\]

The first two switches replace bit 0 by bit 1, while the last two replace
bit 1 by bit 0.  Hence every controller coordinate count is unchanged,
which is stronger than the mod-3 incidence condition.

Neither (6.1) nor (6.2) preserves trace support by itself.  In the router,
the unique controller letters 1801 and 5000 disappear and are replaced by
additional occurrences of 1928 and 4873, exactly accounting for the two new
lower depth-three holes.  Support protection remains a separate endpoint
condition.

## 7. Repeated axis 13: exact comparison and corrected target

The final H20 shore still contains the two `2/1` components

\[
 C_1=\{2676,10868\},\qquad
 C_2=\{19568,27760\},                                        \tag{7.1}
\]

with

\[
 10868=2676\cup\{2^{13}\},\qquad
 27760=19568\cup\{2^{13}\}.                                 \tag{7.2}
\]

Their sole current child cells are

\[
\begin{array}{c|c|c|c}
\text{root/child}&\text{cell}&\text{depth/start}&P\text{-tuple}\\ \hline
2676/10868&16890&2/4015&(10788,8804,8308)\\
19568/27760&17819&2/4944&(10352,11360,25696).
\end{array}                                                     \tag{7.3}
\]

Both cells can already be shrunk literally to their roots:

\[
\begin{aligned}
(10788,8804,8308)&\longmapsto(2596,612,116),\\
(10352,11360,25696)&\longmapsto(2160,3168,17504).
\end{aligned}                                                   \tag{7.4}
\]

The first bit-13 run is positions 4014 through 4020 and the second is 4936
through 4955, so every affected central window retains bit 13 outside the
edited triple.  The first shrink also meets the selected cell for target
9588, but that pin retains bit 13 at positions 4018 and 4019; the second
meets no other selected final-DM interval.

Nevertheless (7.4) is matching-neutral.  Each component has only one child
provider, so repinning it from the child to the root merely exchanges which
of the two targets is exposed.  The exact local object missing from each
component is a **second distinct provider for the child**.  Once such a
provider exists and the survival condition holds, Theorem 4.1 saturates the
component.  A native root ear is sufficient but not necessary.

For both components simultaneously, four distinct cells are necessary:
one retained child and one root-repinned duplicate for each component.  The
shared axis makes Theorem 4.2 available, but it does not supply the two
missing cells, preserve an exterior matching, or impose any seam-current
identity.  In particular, the fact that the target flags share axis 13 does
not imply that a contemplated braid carries axis-13 turn current.

### Proposition 7.1 (canonical-H21 one-braid native-ear no-go)

Consider every `FF/RF/FR/RR` three-cut segment-braid description from the
canonical Hall-21 carrier which is Johnson-legal, depth-three resident, and
complete in every upper layer.  There are 9185 such descriptions.  Exactly
one has a depth-one native trace 2676 while retaining depth-two native traces
10868 and 27760; exactly one has a depth-one native trace 19568 while
retaining both children; none has both root ears.

The two exceptional endpoints are

\[
\begin{array}{c|c|c|c|c}
\text{move}&\text{new root interval}&\nu&\text{deficiency}&z\\ \hline
\operatorname{FR}(734,1758,6432)&19568@735&16360&23&9\\
\operatorname{FF}(1165,4232,5611)&2676@5612&16361&22&8.
\end{array}                                                     \tag{7.5}
\]

Their complete lower-hole vectors are respectively

\[
 (7,17,9,1,0,0,0),\qquad(6,17,9,1,0,0,0),                    \tag{7.6}
\]

and every upper-hole count is zero.  Their zero sets are

\[
\begin{split}
\{&1651,5801,13616,13620,17738,19507,20065,21641,29776\},\\
\{&2654,2804,5801,13616,13620,17738,21641,29776\}.
\end{split}                                                     \tag{7.7}
\]

Hence no single protected braid in this catalogue creates both useful native
ears, and even the two one-ear endpoints increase the number of zeros.

#### Audit

The H100 scanner exhausts the exact cut/orientation loops, materializes each
legal segment permutation, and tests residence and every upper layer.  The
independent filter computes the maximal erosion word and every depth-one and
depth-two native trace.  A separate replay reconstructs the two full compiler
graphs and independently verifies (7.5)--(7.7).  The proposition concerns
the canonical H21 source and the stronger native-ear normal form only.  It
does not exclude a nonnative duplicate-child split from H20 or from a routed
H20 endpoint.

## 8. Sharp remaining boundary

The exact lessons are:

1. Candidate 0575 manufactures a smaller positive circuit; it is not itself
   the splitter.
2. The improving braid discharges root 1801 by a Boolean-square fibre split
   and duplicate-child root shrink on axis 5, not by a native root ear and
   not on repeated axis 13.
3. The fixed-basis local splitter is exactly a `2 x 2` matching condition;
   global rank also requires a target- and cell-disjoint exterior matching.
4. Literal completion is exactly the duplicate-child survival condition in
   one common word.  The H20 instance supplies 682 simultaneous pins, not a
   global 16,363-pin word.
5. The two axis-13 components already pass the local shrink test.  Their
   missing resource is duplicate child capacity, not a way to delete bit 13.
6. The six `1/0` components are untouched.  For a singleton zero component
   there is no child to duplicate; one must create a genuinely new incident
   cell and preserve a disjoint exterior matching.

For the candidate-0575 mechanism, the next proof-safe H20 target would be a
protected router which creates a duplicate native child satisfying Theorem
4.1 for one remaining nonzero component, or a paired version satisfying
Theorem 4.2 and the full exterior ledger.  A route through the six singleton
zeros still needs a different creator mechanism.

The global frontier has since moved independently through

\[
 H20/z6\xrightarrow{\operatorname{RF}(180,2764,4210)}H20/z6
 \xrightarrow{\operatorname{FR}(123,722,4710)}H19/z6.
\]

That route fuses two bases into a two-root native forest and then duplicates
the profile \(\{24610,25634\}\) to discharge a remote component.  It is
another manifestation of duplicate-provider geometry, but its proof and
audit belong to `MATH_K15_DM_PROFILE_ROUTER_H19_20260728.md`; they are not
used to prove any statement in this report.

## 9. Reproducibility

The literal root-1801 certificate and verifier are

```text
b8adf3d749c72d8ad57e8d7b1756f1ad8316b0a4110023bf61b43e53499affb6
  scratch/k15_h21_h20_rooted_native_common_q_certificate.json
a0d2db6ee712ac309f2f9c94bf07ca2be467e9cd729658ac8ad8ac1413b027e9
  scratch/audit_k15_h21_h20_rooted_native_common_q.py
```

The repeated-axis census and its independent candidate replay are

```text
1de4be5c1e478a0aaa1deb3fdcd855b9dcb70063b28aa518338332511d5da6cc
  scratch/k15_h21_axis13_one_braid_native_ear_census.json
f8d54085d0383e6bee368567443178d60a4319a5c221a0eddf84ae31002dee4b
  scratch/audit_k15_h21_axis13_useful_ear_census.py
f9093cf8dafe514ea5499fbe97e4a003a0134b3cc24fa3f536b1520c32cdc146
  scratch/audit_k15_h21_axis13_useful_ear_census.json
```

The exhaustive scanner/filter sources are

```text
6d9035232f9cb69134286dc19e7d33582e2c893748161058f3b3c193fbea7b2f
  scratch/search_k15_graded_portal_native.cpp
93ab83d13676c76d0559a595f42dd60592b8ba0ee22457520c73e913a6779221
  scratch/filter_k15_double_native_ears.py
```

The full H100 upper-safe move log had 9186 lines (9185 move descriptions plus
the summary) and SHA-256

```text
1e2c48d9d4ee667e9320f8cc86f5ae269f1d68c0a015f3fee5791b4a2b1c2cc6.
```

The replay script performs no cut enumeration.  It was run on the H100 CPU,
as required, and reconstructs only the two reported endpoint graphs.
