# Pascal reroots: the exact cut-transversal redundancy theorem

Date: 2026-07-31  
Lane: A, reroot/upper shadow  
Status: exact dimension-uniform criterion proved; the q1-only uniform
implication is refuted; existence for full Pascal sources remains conditional

## 0. Verdict

The stated one-defect Pascal hypotheses give exact middle ownership and, in
the interior case, two marked q1 holes.  A dimension-uniform upper-safe
reroot requires one further assertion, identified exactly below.  Installing
the two q1 colours is only the first ledger; whether every full Pascal source
admits a reroot satisfying the additional assertion remains open.

The exact missing invariant is targetwise.  A block reroot chooses old cut
positions.  An old upper target is endangered precisely when those cuts meet
the span of **every** old interval witnessing that target.  The target then
has to be reproduced by a new cross-block ladder.  Thus the exact condition is

\[
 \boxed{\text{every target whose old witnesses are all cut occurs in a new
 cross-block ladder.}}                                      \tag{0.1}
\]

This is necessary and sufficient.  It cannot be replaced by average
abundance, total multiplicity, or q1 multiplicity.  A dimension-uniform
Johnson-path counterfamily below has a completely successful two-hole q1
reroot, with both deleted q1 colours redundant, but loses two higher targets.
A second counterfamily has literally unique higher witnesses and admits no
same-deck Johnson rethread satisfying the two designated q1 demands.

These counterexamples refute a theorem whose only hypotheses are the local
two-hole q1 ledger and pointwise q1 redundancy.  Their designated q1 palette
is not the complete Boolean q1 layer, so they do **not** refute a stronger
theorem using full q1 completeness and all global Pascal identities.  For
that stronger theorem, (0.1), together with Johnson-legal new seams, is the
minimum presently unproved hypothesis.

## 1. Witness spans and block reroots

Let

\[
 T=(T_0,\ldots,T_{N-1})
\]

be a word of rank-\(r\) subsets of a ground set.  For \(0\le i\le j<N\),
write

\[
 J_T(i,j)=\bigcup_{p=i}^{j}T_p
\]

and associate to this interval its set of internal cut positions

\[
 \partial[i,j]=\{i,i+1,\ldots,j-1\}\subseteq\{0,\ldots,N-2\}. \tag{1.1}
\]

For a target \(Z\), define its old occurrence-labelled witness-span multiset

\[
 \mathcal H_T(Z)=
 \{\!\{(i,j;\partial[i,j]):J_T(i,j)=Z\}\!\}.             \tag{1.2}
\]

The interval label \((i,j)\) is retained even when two spans coincide (which
can occur for singleton intervals).  Whenever only hitting is discussed
below, \(\mathcal H_T(Z)\) may be read as the underlying interval multiset.

A **block reroot** chooses a cut set

\[
 C\subseteq\{0,\ldots,N-2\},                             \tag{1.3}
\]

cuts \(T\) there into consecutive nonempty blocks, and concatenates those
blocks in a new order, each block independently forward or reversed.  Let
\(R\) be the resulting word.  An interval of \(R\) is **internal** if it lies
inside one transported block, and **crossing** otherwise.  Let

\[
 i_C(Z)=\#\{(i,j;H)\in\mathcal H_T(Z):H\cap C=\varnothing\} \tag{1.4}
\]

and let \(x_R(Z)\) be the number of crossing intervals of \(R\) whose union
is \(Z\), counted with multiplicity.

### Theorem 1.1 (multiplicity-exact cut/ladder identity)

For every target \(Z\),

\[
                    m_R(Z)=i_C(Z)+x_R(Z),                \tag{1.5}
\]

where \(m_R(Z)\) is the number of all interval witnesses of \(Z\) in \(R\).

Consequently, for any required target family \(\mathcal U\), put

\[
 \mathcal V_T(C)=
 \{Z\in\mathcal U:C\cap H\ne\varnothing
       \text{ for every }(i,j;H)\in\mathcal H_T(Z)\}.    \tag{1.6}
\]

The block reroot covers every member of \(\mathcal U\) if and only if

\[
 \boxed{\mathcal V_T(C)\subseteq\operatorname{supp}x_R.} \tag{1.7}
\]

An originally missing target has \(\mathcal H_T(Z)=\varnothing\), so it
belongs to \(\mathcal V_T(C)\) by vacuity.  Thus (1.7) simultaneously says:

1. every old target whose last old witness was cut is recreated; and
2. every old hole is installed.

#### Proof

An old interval survives as an internal interval precisely when no chosen
cut lies in its span.  Transporting or reversing its block preserves its
union, and gives a multiplicity-preserving bijection between such old
intervals and the internal intervals of \(R\).  Every remaining interval of
\(R\) is crossing and contributes to \(x_R\).  This proves (1.5), and (1.7)
is the assertion \(m_R(Z)>0\) for every \(Z\in\mathcal U\). \(\square\)

For a displayed block order \(C_1\Vert\cdots\Vert C_s\), the crossing bank
in (1.5) is completely explicit.  A crossing interval beginning in \(C_a\)
and ending in \(C_b\), \(a<b\), has union

\[
 \operatorname{OR}(\operatorname{suf} C_a)\ \cup\!
 \bigcup_{a<t<b}\operatorname{OR}(C_t)\ \cup\!
 \operatorname{OR}(\operatorname{pre} C_b).             \tag{1.8}
\]

Thus (1.7) is a finite literal certificate, not an existence heuristic.

### Corollary 1.2 (two endpoint blocks)

For

\[
 T=A\Vert B\Vert C_0,
 \qquad R=\operatorname{rev}A\Vert B\Vert\operatorname{rev}C_0,
\]

the new crossing support is exactly

\[
\begin{aligned}
 &(P(A)\vee P(B))
 \ \cup\ (S(B)\vee S(C_0))\\
 &\qquad\cup\bigl(P(A)\vee\{W(B)\}\vee S(C_0)\bigr),   \tag{1.9}
\end{aligned}
\]

where \(P,S,W\) are the prefix, suffix and whole-block union families and
\(\vee\) means pairwise union.  Here \(P\) and \(S\) contain only nonempty
prefixes and suffixes.  A higher target survives exactly when it has an old
witness inside one of the three blocks or belongs to (1.9).

## 2. Exact redundancy is an interval-transversal number

For an old covered upper target \(Z\), define

\[
 \tau_T(Z)=\min\{|D|:D\cap H\ne\varnothing
            \text{ for every }(i,j;H)\in\mathcal H_T(Z)\}. \tag{2.1}
\]

This is the number of cut positions needed to destroy every internal witness
of \(Z\).  Because \(Z\) is an upper target of rank greater than \(r\), all
of its witness spans are nonempty.

### Lemma 2.1 (interval packing equals interval piercing)

\(\tau_T(Z)\) equals the maximum number of pairwise disjoint nonempty
witness spans in \(\mathcal H_T(Z)\).

#### Proof

This is the elementary interval-piercing theorem.  Repeatedly choose a span
with smallest right endpoint, put that endpoint into \(D\), and delete every
span containing it.  The spans chosen by the algorithm are pairwise
disjoint, while the selected endpoints hit every span.  Any hitting set must
use a different point for each pairwise disjoint span.  The two numbers are
therefore equal. \(\square\)

### Theorem 2.2 (sharp black-box redundancy radius)

Every block reroot using at most \(b\) old cut positions preserves \(Z\)
internally whenever

\[
                         \tau_T(Z)\ge b+1.               \tag{2.2}
\]

This is sharp for an internal-survival guarantee uniform over all choices of
\(b\) cuts and independent of new ladders.  For a specified cut set \(C\),
the exact weaker total-survival condition is

\[
 C\text{ is not a transversal of }\mathcal H_T(Z)
 \quad\text{or}\quad x_R(Z)>0.                          \tag{2.3}
\]

In particular, if \(Z\) has one interval witness \([i,j]\), then

\[
 C\cap\partial[i,j]=\varnothing
 \quad\text{or}\quad x_R(Z)>0                           \tag{2.4}
\]

is necessary and sufficient.

#### Proof

If \(|C|\le b<\tau_T(Z)\), then \(C\) cannot meet every witness span, so
one witness is internal.  If \(\tau_T(Z)\le b\), a transversal of at most
\(b\) cuts exists, showing sharpness.  Formula (2.3) is Theorem 1.1. \(\square\)

A composition of \(h\) two-ended segment reroots has a common refinement
with at most \(2h\) old breakpoints.  Hence

\[
             \tau_T(Z)\ge 2h+1                           \tag{2.5}
\]

protects \(Z\) internally against every such composition.  For one
two-ended reroot, three pairwise cut-disjoint witnesses suffice.

### Corollary 2.3 (exact bounded-reroot number)

Let \(\mathcal R_h(T)\) be the chronologies obtainable from \(T\) by at most
\(h\) two-ended segment reroots, let \(C_R\) be the common-refinement cut
set of \(R\), and let \(\mathcal U_1\) be the required adjacent-q1 palette.
Write \(\mu_1(R)\) for the adjacent-union multiset.  Within this move class,
the exact minimum is

\[
\begin{aligned}
h_{\min}=\min\{h:\ &\exists R\in\mathcal R_h(T)
 \text{ with Johnson-legal seams},\\
&\mathcal U_1\subseteq\operatorname{supp}\mu_1(R),\quad
 \mathcal V_T(C_R)\subseteq\operatorname{supp}x_R\}.     \tag{2.6}
\end{aligned}
\]

Thus “boundedly many reroots suffice” precisely when the set in (2.6) is
nonempty for a bounded \(h\).  This is not a monotone set-cover problem:
adding a cut can create a new liability by hitting the last witness of a
different target.

The distinction from average abundance is exact: a target can have
arbitrarily many nested or mutually overlapping witnesses but
\(\tau_T(Z)=1\).  One cut then destroys all of them.  Multiplicities of
other targets are irrelevant.

## 3. Fixed-window seam capacity

Suppose every final block has length at least \(D\).  At fixed depth \(q\),
meaning windows of exactly \(q+1\) middle states, one new seam contributes
exactly \(q\) crossing windows.  If the final common refinement has \(b\)
seams, define \(\mathcal D_q\) to be the union of:

1. the old depth-\(q\) holes; and
2. old depth-\(q\) targets for which every fixed-window witness is cut.

The exact fixed-window condition is that the new depth-\(q\) seam ladders
cover \(\mathcal D_q\).  Consequently the necessary bounds are

\[
 |\mathcal D_q|\le bq,
 \qquad
 \sum_{q=1}^{D}|\mathcal D_q|
       \le b\binom{D+1}{2}.                              \tag{3.1}
\]

For \(h\) two-ended reroots, \(b\le2h\), so

\[
 |\mathcal D_q|\le2hq,
 \qquad
 \sum_{q=1}^{D}|\mathcal D_q|\le hD(D+1).               \tag{3.2}
\]

These counts are not sufficient: the literal OR values must be the required
targets.  They also do not apply to arbitrary-width witnesses of a given
rank.  For the complete upper tower without a geodesic fixed-window theorem,
the arbitrary-width criterion (1.7) is the fail-safe statement.

This quantifies the valid \(O(D)\)-seam conclusion.  Such a bound follows
when the vulnerable/defect tower is actually covered by \(O(D)\) literal
boundary ladders, for example by \(O(D)\) nested rays.  It does not follow
from the number of q1 defects.

## 4. Specialization to the one-defect Pascal lift

Let \(|\Omega_0|=2r-1\), let \(z\notin\Omega_0\), and write

\[
 P_i=D^{h-1}w_i\quad(0\le i\le N),\qquad
 Q_i=D^hw_i\quad(0\le i<N),
 \qquad N={2r-1\choose r}.                              \tag{4.1}
\]

Assume

\[
 Q_i=P_i\cup P_{i+1},                                   \tag{4.2}
\]

the \(Q_i\) are all old rank-\(r\) sets once, and deleting the indexed
occurrence \(P_c\) leaves all old rank-\((r-1)\) sets once.  Then

\[
 T_P=\operatorname{rev}(z\cup P_{[0,c)})\Vert Q
     \Vert\operatorname{rev}(z\cup P_{(c,N]})           \tag{4.3}
\]

owns every child middle set once.  All its Johnson adjacencies are automatic
except possibly \(Q_{c-1}Q_c\), which is legal exactly when

\[
 |Q_{c-1}\cap Q_c|=r-1.                                \tag{4.4}
\]

For \(2\le c\le N-2\), its forced marked q1 holes are

\[
 \alpha=z\cup Q_{c-1},\qquad \beta=z\cup Q_c.           \tag{4.5}
\]

There is a canonical two-seam installation.  Its new seam colours are
\(\alpha,\beta\), while its deleted old unmarked seam colours are

\[
 \gamma_-=Q_{c-2}\cup Q_{c-1},\qquad
 \gamma_+=Q_c\cup Q_{c+1}.                              \tag{4.6}
\]

Endpoint cases have the evident one-sided truncation.

### Theorem 4.1 (exact Pascal q1 redundancy condition)

Assume that the natural child is otherwise q1-complete and that
\(\alpha\ne\beta\) are absent.  Also assume the proposed chronology is
Johnson legal, including the exceptional test (4.4).  Let \(m_1(U)\) be the
old adjacent-colour multiplicity and put

\[
 d(U)=\mathbf1[\gamma_-=U]+\mathbf1[\gamma_+=U].         \tag{4.7}
\]

The canonical two-seam installation is q1-complete if and only if

\[
                    m_1(U)\ge d(U)+1                    \tag{4.8}
\]

for every old required q1 colour \(U\).

Thus distinct \(\gamma_-,\gamma_+\) must each have multiplicity at least
two.  If they coincide, that colour must have multiplicity at least three.

#### Proof

The two new seam occurrences are committed to the two distinct old holes.
Every old colour \(U\) therefore has post-reroot multiplicity
\(m_1(U)-d(U)\).  Positivity for every old colour is exactly (4.8), while
the two new seams install \(\alpha,\beta\). \(\square\)

### Theorem 4.2 (minimum all-depth Pascal hypothesis)

Let \(C_P\) be the old cut set of a proposed Johnson-legal Pascal reroot and
let \(x_P\) be its complete new cross-block interval bank.  The reroot is
upper-complete exactly when

\[
                  \boxed{\mathcal V_{T_P}(C_P)
                         \subseteq\operatorname{supp}x_P.} \tag{4.9}
\]

For the canonical two-seam q1 repair, (4.9) must be imposed together with
(4.8).  Equivalently, every old higher target must have an uncut witness or
an exact new ladder witness, and every old higher hole must have an exact new
ladder witness.

#### Proof

This is Theorem 1.1 applied to the Pascal child. \(\square\)

No lower bound on \(\tau_{T_P}(Z)\) for higher \(Z\), and no proof of (4.9),
is presently derived from (4.1)--(4.5).  Thus the proved automatic Pascal
output is the two-hole q1 normal form; an all-depth absorber remains an
additional construction problem.

## 5. A q1-safe reroot that loses higher shadows

Write \(ab=\{a,b\}\), allowing spaces for two-digit coordinates.  In
\(J(12,2)\), let

\[
\begin{aligned}
T={}&(16,15,25,24,34,13,14,45,4\,10,10\,11,7\,10,79,\\
    &\hspace{34mm}9\,10,8\,10,8\,11,7\,11,7\,12).
                                                               \tag{5.1}
\end{aligned}
\]

All vertices are distinct and consecutive vertices intersect in one point.
Cut after positions 4 and 11, and put

\[
 R=\operatorname{rev}T[0,4]\Vert T[5,11]
   \Vert\operatorname{rev}T[12,16].                     \tag{5.2}
\]

The complete signed q1 change is

\[
 \mu_1(R)=\mu_1(T)-\delta_{134}-\delta_{\{7,9,10\}}
             +\delta_{136}+\delta_{\{7,9,12\}}.         \tag{5.3}
\]

The deleted colour \(134\) also occurs on the internal edge \(13|14\),
and \(\{7,9,10\}\) also occurs on \(7\,10|79\).  Each therefore had
multiplicity two.  The two added colours were absent.  Relative to

\[
 \mathcal Q=\operatorname{supp}\mu_1(T)
              \cup\{136,\{7,9,12\}\},                  \tag{5.4}
\]

the old word has exactly two q1 holes and the reroot has none, without
losing any old q1 colour.

Nevertheless let

\[
 U_1=1234,\qquad U_2=\{7,8,9,10\}.                      \tag{5.5}
\]

The unique maximal \(U_1\)-compatible run in \(T\) is

\[
                         (24,34,13,14).                  \tag{5.6}
\]

Every interval witnessing \(U_1\) crosses the cut \(34|13\).  In \(R\),
this run splits into compatible runs with joins \(234\) and \(134\), so
\(U_1\) is absent.  Similarly, the unique maximal \(U_2\)-compatible run is

\[
                     (7\,10,79,9\,10,8\,10),            \tag{5.7}
\]

all its witnesses cross \(79|9\,10\), and after rerooting its two pieces
have joins \(\{7,9,10\}\) and \(\{8,9,10\}\).  Hence \(U_2\) is absent.

This is precisely the failure \(U_1,U_2\in\mathcal V_T(C)\) but
\(x_R(U_1)=x_R(U_2)=0\).

Adding a common core of size \(r-2\) to every displayed pair, and adding
\(r-10\) unused coordinates, embeds the same example in central
\(J(2r,r)\) for every \(r\ge10\).  Therefore q1 redundancy does not become
an upper-shadow theorem in large dimension.

## 6. A same-deck rethread obstruction with unique higher witnesses

The preceding example concerns the natural two-ended reroot.  The following
one shows that bounded same-deck rethreading cannot be guaranteed from the
same q1 data either.  In \(J(12,2)\), take

\[
\begin{aligned}
S={}&(25,56,16,12,23,34,45,4\,11,8\,11,11\,12,7\,12,\\
    &\hspace{42mm}78,89,9\,10,10\,11).                  \tag{6.1}
\end{aligned}
\]

Set

\[
 H_1=235,\quad H_2=\{8,9,11\},\qquad
 U_1=1234,\quad U_2=\{7,8,9,10\}.                      \tag{6.2}
\]

Relative to \(\operatorname{supp}\mu_1(S)\cup\{H_1,H_2\}\), the only q1
holes are \(H_1,H_2\).  The sole interval witnessing \(U_1\) is

\[
                         (12,23,34),                     \tag{6.3}
\]

while the only vertices of the deck contained in \(H_1\) are \(25,23\).
Thus any Johnson path on this same vertex deck that installs \(H_1\) must
use edge \(25|23\).  Retaining \(U_1\) requires all three vertices in
(6.3) consecutively.  Since \(12\) and \(34\) are disjoint, their only
Johnson ordering is \(12|23|34\), or its reverse.  The vertex \(23\) would
then have degree three, a contradiction.

Symmetrically, the sole witness of \(U_2\) is

\[
                       (78,89,9\,10),                    \tag{6.4}
\]

whereas installing \(H_2\) forces edge \(8\,11|89\).  Again \(89\) would
need degree three.  Therefore no Johnson path on this vertex deck installs
both q1 holes while retaining both unique higher targets.  The same common-
core lift embeds this obstruction in central \(J(2r,r)\) for every
\(r\ge10\).

This does not obstruct a construction that changes the vertex deck or uses
additional physical states.  It proves that a bounded rethread theorem also
needs a provider-degree or cut/ladder hypothesis; q1 hole count alone is
insufficient.

## 7. Consequence for the K17 opposite-choice core

For the frozen K16 parent, the K17 fixed-occurrence lane has the exact core

\[
 O(0x0bf5)=\{9176,10616\},                               \tag{7.1}
\]

where target \(0x1bf5\) forces the first occurrence and target \(0x0ff5\)
forces the second.  Choosing endpoint representatives from the unchanged q1
occurrence deck cannot remove this contradiction.

A bounded block rethread is a genuine escape only if it changes the guard
formula for at least one of those targets: it must create a new seam
occurrence usable in a feasible target interval, create an alternative
provider for the forced missing coordinate, or change the blocker order so
that a new feasible interval appears.

Here is the exact shore-separated proof interface.  Let \(O_R(c)\) be the
positions of q1 colour \(c\) after the rethread.  It is sufficient that:

1. the rethread preserves the exact middle deck and all new seams are Johnson
   legal;
2. every \(O_R(c)\) is nonempty and there are choices \(x_c\in O_R(c)\), one
   for every required q1 colour,
   such that for every required \(z\)-free upper target \(S\) there is a
   physical interval \(I\) with

   \[
   x_c\notin I\quad(c\nsubseteq S),\qquad
   \bigcup_{\substack{c\subseteq S\\x_c\in I}}c=S;       \tag{7.2}
   \]

3. \(\mathcal V_T(C)\subseteq\operatorname{supp}x_R\), so the rethreaded
   parent retains every old upper target and the tagged shore \(z\cup R\)
   inherits every required \(z\)-containing upper target internally.

Condition (7.2), with quantifiers
\(\exists(x_c)\ \forall S\ \exists I\), is the exact simultaneous guard
formula for the untagged shore.  Condition 3 is the exact inherited-shore
criterion if witnesses containing \(z\) are required to lie internally in
the tagged shore.  It is only sufficient in an unrestricted concatenation,
because an interval crossing the untagged/tagged seam can occasionally
replace a lost tagged-shore witness.

Indeed, if \(A_x\) is the selected untagged q1 word and the final shore order
is \(A_x\Vert(z\cup R)\), then the exact condition for a \(z\)-containing
target \(z\cup Z\) is

\[
 Z\in\operatorname{IntOR}(R)
 \ \cup\
 \bigl(\operatorname{SuffixOR}(A_x)
       \vee\operatorname{PrefixOR}(R)\bigr).             \tag{7.3}
\]

For the reverse shore order, replace the second term by
\[
 \operatorname{SuffixOR}(R)\vee\operatorname{PrefixOR}(A_x). \tag{7.4}
\]

Thus condition 2 together with (7.3) or (7.4), rather than condition 3, is
the necessary-and-sufficient test for unrestricted two-shore upper coverage.

Thus 1--3 give a rigorous sufficient carrier/upper-shadow theorem for the
shore-separated Pascal architecture, but not a full K17 word: the run
staircase, lower compiler, and common-Q cap remain separate.  No bounded
rethread satisfying 1--3 is constructed here.  The remaining K17 task is an
occurrence-geometry construction, not another endpoint-representative
choice.

## 8. Exact proved/conditional boundary

Proved:

1. the multiplicity identity (1.5) and iff condition (1.7);
2. the interval-transversal redundancy radius (2.2)--(2.5);
3. the fixed-window seam-capacity bounds (3.1)--(3.2);
4. the exact Pascal q1 multiplicity condition (4.8);
5. the minimum all-depth Pascal condition (4.9);
6. dimension-uniform counterfamilies showing that a local two-hole q1 ledger
   on a designated palette does not imply an upper-safe reroot or same-deck
   rethread.

Not proved:

1. that every full Pascal source has a bounded Johnson-legal reroot satisfying
   (4.9);
2. that its vulnerable higher targets lie on \(O(D)\) boundary rays; or
3. that the K17 fixed-parent opposite-choice core admits such a rethread.

That is the sharp theorem boundary.  The reusable positive statement is not
“two q1 defects imply a safe reroot,” but the cut-transversal/new-ladder
criterion (1.7).
