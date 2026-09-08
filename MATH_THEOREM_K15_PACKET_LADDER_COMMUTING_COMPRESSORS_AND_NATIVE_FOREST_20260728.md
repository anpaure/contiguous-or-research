# Packet ladders, commuting compressors, and multi-root native forests

Date: 2026-07-28

Status: exact abstract theorems; exact specialization to the two certified
Hall-20 top compressors, their commuting carrier square, and the verified
Hall-20-to-Hall-19 native-forest route. No further packet search is
performed here. A second star-to-fan rung and its terminal physical
splitter remain unproved.

## 0. Verdict

The two best Hall-20 top compressions are the same internal native-basis
exchange:

\[
37/36\longrightarrow5/4.
\tag{0.1}
\]

The old target branch is a full rank-at-most-two star above a rank-five base
on eight free axes:

\[
1+8+\binom82=37.
\tag{0.2}
\]

The new fan has rank-layer counts \((1,1,3)\), hence five targets. Both
branches have gap one, so their native bases have sizes 36 and 4. Therefore
the containing component loses exactly

\[
37-5=36-4=32
\tag{0.3}
\]

targets and cells, while retaining the same global root and unit deficit:

\[
161/160\longrightarrow129/128.
\tag{0.4}
\]

The number 32 is caused by the star-to-fan signature, not by packet length
15 alone.

There are two distinct ladder statements.

1. An abstract nonfolding two-rail full-turn packet of length \(p=15\)
   peels \(2(p+1)=32\) balanced vertices. If that complete rail certificate
   recurred, it would predict the route through the last nontrivial,
   square-capable rung
   \[
   161/160\to129/128\to97/96\to65/64\to33/32.
   \tag{0.5}
   \]
   If the same rail hypotheses held once more at (33/32), they would peel
   it to (1/0); the rail theorem itself does not force termination at 33.
2. The concrete star-to-fan signature is sharper. Each certified
   \(129/128\) endpoint is a punctured truncated Boolean ideal. It permits
   at most one further identical \(37/36\to5/4\) exchange, reaching
   \(97/96\); after that the required full star cannot exist. Thus the
   strict packet ladder stops at \(97/96\), not \(33/32\).

The prospective \(97/96\) endpoint has a canonical pendant Boolean square.
It is splittable exactly when the retained common bank exposes a pair
transverse to the proposed two fibre columns. Size and topology alone do
not imply that matching condition or physical seam legality.

The root-960 and root-8217 compressors commute as carrier moves, even though
their short source packets overlap in eleven middle states. Their four FF
moves form an exact block diamond. Both orders have identical endpoint
digest

    5d154551043d7b7551022d07205d70eecba4ea16c546e950f3774e09d216d97c

and canonical DM shore \(613/593\).

Finally, the verified Hall-20-to-Hall-19 router shows that one connected DM
component can have several exposed roots. It fuses the root-8217
\(161/160\) and root-8218 \(160/159\) components into a connected
\(321/319\) native forest with exposed roots \(\{8217,8218\}\) and
structural intersection 8216. The subsequent remote splitter removes the
separate root-24610 \(161/160\) component and gives exact Hall 19 with six
zeros.

## 1. The exact star-to-fan packet

All axes in this note are zero based. For a root \(K\), an axis \(x\), and
an eight-element axis set \(C\) disjoint from \(K+x\), define

\[
\Sigma(K;x,C)=
\{K\cup\{x\}\cup U:U\subseteq C,\ |U|\le2\}.
\tag{1.1}
\]

For pairwise distinct axes \(y,h,q_1,q_2,q_3\), all outside \(K\), define

\[
\Phi(K;y;h;q_1,q_2,q_3)=
\{K+y,\ K+y+h,\ K+y+h+q_i:1\le i\le3\}.
\tag{1.2}
\]

Here plus denotes adjoining the named axes. The target-layer vectors,
relative to a rank-four \(K\), are

\[
\Sigma:(1,8,28),\qquad \Phi:(1,1,3)
\tag{1.3}
\]

in ranks \(5,6,7\).

### Theorem 1.1 (star-to-fan internal basis replacement)

Let \(C^-=(X^-,Y^-)\) and \(C^+=(X^+,Y^+)\) be connected rooted native
components with the same global root \(K\), each of gap one. Suppose

\[
X^-\setminus X^+=\Sigma(K;x,C),\qquad
X^+\setminus X^-=\Phi(K;y;h;q_1,q_2,q_3),
\tag{1.4}
\]

and the corresponding old-only and new-only native basis cells number 36
and 4. Then:

1. both component shores decrease by exactly 32;
2. the component target-layer change is
   \[
   (0,0,-7,-25)
   \tag{1.5}
   \]
   in ranks \(4,5,6,7\);
3. the component remains gap one and retains root \(K\); and
4. this local replacement makes no global Hall claim by itself. Global
   neutrality follows only if a full-graph certificate absorbs the expelled
   balanced layer into the exterior matching, equivalently if the complete
   common-profile contraction proves unchanged global rank and no new
   deficient component appears.

#### Proof

Equation (1.1) has \(1+8+\binom82=37\) targets, while (1.2) has five.
Their native bases have one fewer cell each. This proves the equal
32-decrement on both shores. Rank five loses and gains one target; rank six
loses eight and gains one; rank seven loses 28 and gains three. This is
(1.5). The rooted-native hypotheses give rank one less than target size on
both complete components. The last assertion is precisely the additional
global matching hypothesis stated there; it is not a consequence of the
local cardinalities. \(\square\)

For \(f\) free axes, the analogous numerical decrement is

\[
\left(1+f+\binom f2\right)-5
=f+\binom f2-4.
\tag{1.6}
\]

Only \(f=8\) has a certified physical carrier here.

### Theorem 1.2 (conditional two-rail packet peel)

Let a legal carrier move transport a packet of \(p\) middle states. After
contracting a common exterior matching, suppose its old/new alternating
overlay at one fixed root has:

1. at every gap \(0\le j\le p\) and rail \(\epsilon\in\{0,1\}\)
   there is one target-cell pair \((x_{j,\epsilon},y_{j,\epsilon})\);
2. all \(2(p+1)\) target vertices and all \(2(p+1)\) cell vertices in
   those pairs are globally distinct;
3. no off-ladder incidence reconnecting an expelled rail to the residual
   critical component;
4. rooted unit components before and after the move;
5. a perfect exterior matching of the expelled balanced rail layer; and
6. no change in any other deficient component and no creation of a new
   deficient component.

Then the move peels

\[
m=2(p+1)
\tag{1.7}
\]

targets and cells:

\[
(s,s-1)\longmapsto(s-m,s-m-1),
\tag{1.8}
\]

and is globally matching-neutral.

#### Proof

There are \(p+1\) packet gaps and two rails. Conditions 1--3 make the
resulting \(2(p+1)\) target vertices and \(2(p+1)\) cell vertices distinct
and detach them from the residual alternating component. Condition 5 matches that balanced
layer. The residual component keeps gap one, and condition 6 makes this
the entire global change. \(\square\)

For \(p=15\), (1.7) gives 32. A full-turn removal-colour word is an
independent chronology condition and does not imply the rail hypotheses.
This rail theorem explains the abstract
expectation (0.5), but its nonfolding hypotheses must be reverified at every
rung. The exact set-system theorem below shows that the present star-to-fan
packets lose recursive full-turn persistence after at most one further
rung.

## 2. The two certified Hall-20 compressors

Let \(P_{20}\) be the frozen Hall-20/six-zero carrier, with SHA-256

    9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1

The two moves are

\[
\begin{aligned}
c0161&=\operatorname{FF}(1784,1799,5170),\\
c0163&=\operatorname{FF}(1788,1803,3103).
\end{aligned}
\tag{2.1}
\]

Their short transported blocks have length 15. Including entry and exit,
their removal-colour words are cyclic rotations of one full turn:

\[
(2,12,11,10,9,8,7,6,0,4,3,13,1,5,14,2)
\tag{2.2}
\]

and

\[
(9,8,7,6,0,4,3,13,1,5,14,2,12,11,10,9).
\tag{2.3}
\]

Thus the 16 packet-adjacent gaps (entry, 14 internal gaps, and exit) use
every coordinate once, with the first coordinate repeated at the end. The
fixed roots are four consecutive
removal colours:

\[
960=\{9,8,7,6\},\qquad8217=\{0,4,3,13\}.
\tag{2.4}
\]

### Theorem 2.1 (exact packet parameters)

The move \(c0161\) is Theorem 1.1 with

\[
\begin{aligned}
K&=960,&x&=0,&C&=\{1,2,3,5,11,12,13,14\},\\
y&=4,&h&=3,&\{q_i\}&=\{2,5,14\}.
\end{aligned}
\tag{2.5}
\]

It changes only

\[
(161/160)_{960}\longrightarrow(129/128)_{960}.
\tag{2.6}
\]

The move \(c0163\) has

\[
\begin{aligned}
K&=8217,&x&=1,&C&=\{2,7,8,9,10,11,12,14\},\\
y&=5,&h&=14,&\{q_i\}&=\{9,10,11\},
\end{aligned}
\tag{2.7}
\]

and changes only

\[
(161/160)_{8217}\longrightarrow(129/128)_{8217}.
\tag{2.8}
\]

In each case the old and new component target sets overlap in 124 targets,
so the old-only/new-only counts are exactly 37 and 5. Every other deficient
component is unchanged. Each single-compressor endpoint has canonical DM
shore

\[
677/657-32/32=645/625,
\tag{2.9}
\]

and global Hall deficiency 20.

#### Proof

The exact target symmetric differences are (1.1) and (1.2) with the
displayed parameters. Also

\[
161-124=37,\qquad129-124=5.
\]

Theorem 1.1 gives the local component algebra. The independently audited
complete compiler graphs give matching rank 16,363 at both endpoints and
exclude any new deficient component, proving the asserted global
neutrality. \(\square\)

The two carrier artifacts have SHA-256 values

    fdb95c316a3604f23aba75d1360230330743e443306cea5313e866a721d87563
    88c49a713755ba42d3577e2c80ad1c487ff7a9dd0f2f52d25e5af8da02b415c8

respectively.

## 3. The strict ladder and its terminal square

For a nine-axis set \(S\), put

\[
I_3(K,S)=\{K\cup U:U\subseteq S,\ |U|\le3\}.
\tag{3.1}
\]

### Theorem 3.1 (punctured-ideal normal form)

Each compressed \(129/128\) target component has the form

\[
X_1=I_3(K,S)\setminus\{K\cup\tau\},
\qquad |S|=9,\quad|\tau|=3.
\tag{3.2}
\]

The exact data are

\[
\begin{array}{c|c|c}
K&S&\tau\\ \hline
960&\{1,2,3,4,5,11,12,13,14\}&\{1,3,13\}\\
8217&\{2,5,7,8,9,10,11,12,14\}&\{2,12,14\}.
\end{array}
\tag{3.3}
\]

Consequently its target-layer vector is

\[
(1,9,36,83).
\tag{3.4}
\]

#### Proof

The full ideal has layer counts \((1,9,36,84)\). The exact target
comparison shows that its only omitted member is the displayed rank-seven
target \(K\cup\tau\). \(\square\)

### Theorem 3.2 (one further strict rung, but no third)

In (3.2), for \(x\in S\), a full removable star

\[
\Sigma(K;x,S\setminus\{x\})
\tag{3.5}
\]

exists if and only if \(x\notin\tau\). Hence there are exactly six
set-theoretically eligible axes.

Assume further that \(y\notin S\) is fresh and that
\(h,q_1,q_2,q_3\) are pairwise distinct members of \(S\setminus\{x\}\).
If one legal support-closed star-to-fan packet with those parameters realizes
a second rung, the result is a \(97/96\) component with target-layer vector

\[
(1,9,29,58).
\tag{3.6}
\]

Its rank-six support graph on the nine rank-five axes is \(K_8\) plus one
pendant edge \(yh\). Its rank-seven support consists of all triples on the
\(K_8\), except \(\tau\), together with the three triples \(yhq_i\).

No third packet of the same \(37\to5\) signature exists.

#### Proof

The star at \(x\) contains every rank-at-most-three ideal member containing
\(x\). The puncture deletes one of these members exactly when
\(x\in\tau\), proving the first assertion. Subtracting (1.5) again from
(3.4) gives (3.6) and the stated graph/face description.

In that graph only \(h\) is adjacent to all eight other rank-five axes: it
has its seven \(K_8\) neighbours and the pendant neighbour \(y\). Thus only
\(h\) could be the base of another full eight-free-axis star. Such a star
would require all seven triangles \(hyw\), with \(w\) in the other
\(K_8\) vertices. Only the three triangles \(yhq_i\) exist. Hence no full
third star exists. \(\square\)

The exact prospective choices are

\[
\begin{array}{c|c|c}
K&x\text{ eligible}&y\text{ fresh}\\ \hline
960&\{2,4,5,11,12,14\}&\{0,10\}\\
8217&\{5,7,8,9,10,11\}&\{1,6\}.
\end{array}
\tag{3.7}
\]

These are combinatorial choices, not certified carrier moves.

For \(j=0,1,2\), the strict-rung layer formulas are

\[
n_5=9,\qquad n_6=43-7j,\qquad n_7=108-25j,
\tag{3.8}
\]

and satisfy the diagnostic invariant

\[
25n_6-7n_7=319.
\tag{3.9}
\]

The 15-state length by itself implies none of (3.2)--(3.9).

For a cell bank \(B\) on target set \(X\), define

\[
\operatorname{Exp}_2(B)=
\{\{u,v\}\subseteq X:
B\text{ has a matching saturating }X\setminus\{u,v\}\}.
\tag{3.10}
\]

### Theorem 3.3 (rank-only and fixed-basis Boolean-square criteria)

Let a unit-defect component have target set \(X\). Suppose a common retained
bank \(B\) has rank \(|X|-2\). Let the old residual column be \(o\), and let
the new boundary contain two columns \(f_0,f_1\).

The old bank \(B\mathbin{\dot\cup}\{o\}\) has rank \(|X|-1\) if and only
if there is

\[
E_{\rm old}\in\operatorname{Exp}_2(B)
\tag{3.11}
\]

which \(o\) meets. The new bank
\(B\mathbin{\dot\cup}\{f_0,f_1\}\) has rank \(|X|\) if and only if there
is, possibly different,

\[
E_{\rm new}=\{u,v\}\in\operatorname{Exp}_2(B)
\tag{3.12}
\]

such that \(f_0,f_1\) match \(u,v\) distinctly. Therefore, assuming the old
component has rank \(|X|-1\), the replacement raises rank by one exactly
when such an \(E_{\rm new}\) exists.

If one fixes a particular \(B\)-matching and requires an edge-for-edge
pin-preserving splitter, then its one exposed pair \(E\) must satisfy both
conditions simultaneously. This stronger one-pair criterion is sufficient
in general and necessary within that fixed-basis architecture.

For a Boolean square

\[
Q=\{K,K+a,K+b,K+a+b\}
\tag{3.13}
\]

split into parallel fibres, the rank-only criterion says that
\(E_{\rm new}\) must be transverse to the fibre partition. In the
rooted-native duplicate-child architecture with its retained basis, the
fixed exposed pair must be transverse; the canonical choice is the diagonal

\[
E=\{K,K+a+b\}.
\tag{3.14}
\]

#### Proof

The old-rank equivalence follows by adding or deleting the one edge using
\(o\). For the new-rank equivalence, match \(B\) to
\(X\setminus E_{\rm new}\) and the two new columns to its two points; the
converse follows by deleting the two new-column edges from a perfect
matching. The two exposed pairs need not coincide for an abstract rank
gain. They must coincide only when the same retained \(B\)-matching is part
of the certificate. \(\square\)

The root-458 and root-1801 splitters have exposed diagonals

\[
\{458,16846\},\qquad\{1801,1835\},
\tag{3.15}
\]

with common-bank ranks 22 and 23, respectively.

After a prospective second strict rung, the \(97/96\) component has the
canonical pendant square

\[
Q(K;y,h)=\{K,K+y,K+h,K+y+h\}.
\tag{3.16}
\]

This is the exact strict-ladder terminus. It is physically splittable only
if its retained bank exposes a transverse pair as in Theorem 3.3 and the
two fibre cells arise from a legal full-catalogue carrier move.

For a literal common-controller split, the common bank must retain a native
basis for \(X\setminus E\); one new fibre must supply a duplicate child
occurrence which passes the protected root-shrink test, and the other must
supply the top \(K+y+h\). Exterior matching survival and the final all-shore
Hall cut remain separate necessary conditions.

## 4. Commuting packet compressors at carrier level

For a word

\[
T=A\,P\,Q\,R\,S\,U\,D
\tag{4.1}
\]

write

\[
a=|A|,\quad p=|P|,\quad q=|Q|,\quad r=|R|,\quad
s=|S|,\quad u=|U|.
\]

Assume (p,q,r,s,u>0), so every displayed operation is a genuine
three-cut move.

The move \(\operatorname{FF}(i,j,k)\) swaps the blocks \(T[i:j]\) and
\(T[j:k+1]\) without reversal.

### Theorem 4.1 (overlapping-packet FF diamond)

Define

\[
\begin{aligned}
F_1&=\operatorname{FF}
(a,a+p+q,a+p+q+r+s+u-1),\\
F_2&=\operatorname{FF}
(a+p,a+p+q+r,a+p+q+r+s-1).
\end{aligned}
\tag{4.2}
\]

Then

\[
F_1(T)=A\,R\,S\,U\,P\,Q\,D,\qquad
F_2(T)=A\,P\,S\,Q\,R\,U\,D.
\tag{4.3}
\]

On those children put

\[
\begin{aligned}
F_2^{(1)}&=\operatorname{FF}
(a+r,a+r+s,a+r+s+u+p-1),\\
F_1^{(2)}&=\operatorname{FF}
(a,a+p+s+q,a+p+s+q+r+u-1).
\end{aligned}
\tag{4.4}
\]

Then

\[
F_2^{(1)}F_1(T)=F_1^{(2)}F_2(T)
=A\,R\,U\,P\,S\,Q\,D.
\tag{4.5}
\]

#### Proof

The first path swaps \(PQ\) with \(RSU\), then \(S\) with \(UP\). The
second swaps \(QR\) with \(S\), then \(PSQ\) with \(RU\). Both yield
(4.5). \(\square\)

Word equality alone does not prove physical commutation. For an oriented
cut, define its **complete seam signature** to contain:

1. the ordered states needed for Johnson adjacency;
2. every crossing carrier window used by residence and protected-shadow
   ledgers; and
3. with multiplicity, every full compiler-cell shore whose erosion
   dependency crosses the seam.

### Theorem 4.2 (explicit seam condition for physical commutation)

Assume the two initial arrows from (T) are already certified for Johnson
adjacency, residence, every protected occurrence/witness ledger, and the
full compiler constraints. Assume the two adjusted arrows pass their
Johnson tests. Suppose the
complete seam signature of each \(F_i\) is transported unchanged, up to
position translation, to the adjusted arrow \(F_i^{(3-i)}\). More generally,
it is enough that for the complete physical profile multiset \(\mathcal P\)
there are signed
multisets \(\Delta_1,\Delta_2\) satisfying

\[
\begin{aligned}
\mathcal P(F_1T)-\mathcal P(T)&=\Delta_1,&
\mathcal P(F_2T)-\mathcal P(T)&=\Delta_2,\\
\mathcal P(T_*)-\mathcal P(F_1T)&=\Delta_2,&
\mathcal P(T_*)-\mathcal P(F_2T)&=\Delta_1,
\end{aligned}
\tag{4.6}
\]

with the same identities for complete occurrence multisets or named retained
witnesses in every residence and protected-shadow ledger. Signed support
sets alone are not sufficient because support survival is nonlinear.

Then both paths are legal and have the same physical compiler endpoint. If
\(\Delta_1\) and \(\Delta_2\) have disjoint target-and-cell incidence
supports throughout all four states, replace internal branches in disjoint
rooted components, leave all other component banks fixed, and create no
cross-component merger, the two component compressors commute.

#### Proof

Theorem 4.1 gives the common carrier word. Complete signature equality
transports every local legality and protected-ledger certificate. Equation
(4.6) gives endpoint profile multiset
\(\mathcal P(T)+\Delta_1+\Delta_2\) in either order. Disjoint component
support makes the two internal replacements independent. \(\square\)

Disjoint DM target sets alone are insufficient: the source packets may
overlap and their new seams may interfere. The complete seam condition is
the exact extra hypothesis.

### 4.3 The certified Hall-20 square

Take

\[
(a,p,q,r,s,u)=(1784,4,11,4,1301,2067).
\tag{4.7}
\]

The first edges of the square are

\[
\operatorname{FF}(1784,1799,5170),\qquad
\operatorname{FF}(1788,1803,3103),
\tag{4.8}
\]

and the adjusted edges are

\[
\operatorname{FF}(1788,3089,5159),\qquad
\operatorname{FF}(1784,3100,5170).
\tag{4.9}
\]

The shared exact commuting-square certificate states that all four carrier
arrows are legal and have the required component-local effects. The block
identity and common endpoint digest are independently checked here; no
separate four-arrow seam-audit artifact is claimed in this note. Both paths
compress root 960 and root 8217 and end at the same carrier. Its canonical
DM shore is

\[
677/657-2(32/32)=613/593,
\tag{4.10}
\]

and its middle digest is the value in Section 0.

## 5. Multi-root native forests

### Definition 5.1

A **multi-root native forest** is a compiler target/cell pair \((X,Y)\)
with a set \(R\subseteq X\) such that one controller gives a bijection

\[
\tau:Y\overset{\sim}{\longrightarrow} X\setminus R.
\tag{5.1}
\]

Put \(g=|R|\). Then \(|X|-|Y|=g\). Its structural core

\[
\kappa=\bigcap_{x\in X}x
\tag{5.2}
\]

need not be an exposed root. The word forest refers to the simultaneous
native pin family; it does not assert graph-theoretic acyclicity or even
connectedness. A rooted native component is the connected case \(g=1\).

### Theorem 5.2 (forest matching and ears)

Let \((X,Y,R)\) be a gap-\(g\) native forest.

1. Its native atlas is a literal matching of size \(|X|-g\), exposing
   exactly \(R\).
2. A disjoint exterior matching on all targets outside \(X\) combines with
   it to a matching of size \(N-g\), where \(N\) is the target-universe
   size.
3. If one final controller supplies \(t\) additional distinct cells with
   distinct native traces in \(R\), while retaining the atlas and exterior
   matching, the displayed rank rises by \(t\).
4. In the pin-preserving all-native class, the forest becomes perfect if
   and only if all \(g\) roots receive distinct ears.

#### Proof

The bijection (5.1) proves the first assertion. Disjoint matchings unite.
Each new root trace covers one previously exposed target on one new cell.
Conversely, after retaining the atlas, precisely the roots in \(R\) remain
uncovered. \(\square\)

### Theorem 5.3 (neutral fusion)

Suppose a neutral carrier move takes pairwise cell- and target-disjoint
native forests \((X_i,Y_i,R_i)\) and changes their incidence graph so that
their union becomes connected, while preserving the native trace atlas

\[
\bigsqcup_iY_i\longrightarrow
\left(\bigcup_iX_i\right)\setminus\left(\bigcup_iR_i\right).
\tag{5.3}
\]

Then the result is one native forest with root set \(\bigcup_iR_i\), gap
\(\sum_i|R_i|\), and unchanged matching rank.

#### Proof

Equation (5.3) is a bijection omitting exactly the displayed roots.
Connectivity makes the union one component; preserving the same atlas
preserves its rank. \(\square\)

### 5.4 The verified Hall-20-to-Hall-19 route

The exact chain is

\[
H20/z6
\xrightarrow{\operatorname{RF}(180,2764,4210)}H20/z6
\xrightarrow{\operatorname{FR}(123,722,4710)}H19/z6.
\tag{5.4}
\]

The neutral router fuses

\[
(161/160)_{8217}\quad\text{and}\quad(160/159)_{8218}
\tag{5.5}
\]

into one connected \(321/319\) forest. Its structural intersection is 8216,
but its exposed roots are

\[
R=\{8217,8218\}.
\tag{5.6}
\]

Its 319 native traces are exactly its target set minus \(R\). The second
braid remotely removes the separate root-24610 \(161/160\) component. The
final matching rank is 16,364, deficiency is 19, the zero count is six, and
the canonical DM shore is

\[
516/497.
\tag{5.7}
\]

On that fixed 161-target block, 159 restricted profiles cancel and the
exceptional surgery is

\[
\{26146,26402\}\longrightarrow
\{24610,25634\}\mathbin{\dot\cup}\{26146\}
\mathbin{\dot\cup}\{26402\}.
\tag{5.8}
\]

The profile \(\{24610,25634\}\) already had one occurrence, so (5.8)
creates the duplicate needed to match both targets. This is a profile
router/discharge, not a compression of the fused forest.

The cross-state gap matrix is

\[
\begin{pmatrix}
20&20&19\\
20&20&19\\
18&18&19
\end{pmatrix}.
\tag{5.9}
\]

The frozen carrier SHA-256 values are

    9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
    eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51
    86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b

There is also a shore-local common-controller witness: native target 25634
has two physical occurrences, and shrinking one to root 24610 retains the
other, the final 497 forest pins, and the 160 nonroot pins of the discharged
component. Thus one controller realizes 658 pins on the former 677-target
shore. This remains weaker than a common-controller lift of a full
16,364-edge matching.

This is an exact outer compiler-Hall descent. It does not give one global
common-controller matching: the native forest atlas is literal, but the
exterior matching still requires a joint common-\(Q\) lift.

## 6. Proved and unproved boundary

Proved:

1. the exact \(37/36\to5/4\) star-to-fan theorem and decrement 32;
2. its two first-rung specializations at roots 960 and 8217;
3. the punctured-ideal normal form of both \(129/128\) endpoints;
4. exact combinatorial eligibility for one second strict rung and the
   impossibility of a third identical rung;
5. the exposed-pair Boolean-square criterion, including its literal
   duplicate-child refinement;
6. the overlapping-block FF diamond and the complete seam condition for
   physical commutation;
7. the exact two-compressor endpoint \(613/593\);
8. the multi-root native-forest matching, ear, and fusion theorems; and
9. the verified Hall-20-to-Hall-19 forest route.

Not proved:

* a legal second \(37/36\to5/4\) carrier packet from either \(129/128\)
  endpoint;
* a \(97/96\) carrier endpoint;
* the exposed-diagonal matching and legal physical fibre split there;
* the abstract rail ladder to \(33/32\) for these components;
* commutation of component-disjoint compressors without the complete seam
  condition; or
* a common-controller lift of the exterior H19 matching.

## 7. Principal artifacts

    scratch/k15_segment_braid_hall20_zero6.json
    scratch/k15_h20_exact_candidates/candidate_0161.json
    scratch/k15_h20_exact_candidates/candidate_0163.json
    scratch/k15_h20z6_neutral_dm_compression_20260728.json
    scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
    scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
    scratch/audit_k15_h20_to_h19_root8216_chain.json
    MATH_THEOREM_K15_MULTIROOT_NATIVE_FOREST_PROFILE_ROUTER_20260728.md
    MATH_K15_DM_PROFILE_ROUTER_H19_20260728.md

No Kissat, SAT, exhaustive search, or heavy local computation was run for
this note. The commuting digest was checked by the exact block identity
(4.5) using a tiny read-only audit of the frozen path.
