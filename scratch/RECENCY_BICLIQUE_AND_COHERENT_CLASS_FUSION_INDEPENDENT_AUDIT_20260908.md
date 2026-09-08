# Recency bicliques and exact fusion by coherent source classes

Date: 2026-09-08. Independent pure-proof audit by `exact_b_induction`
of the user's proposed gadget and fusion theorem.

Status: the algebraic gadget and the one-path-plus-cycles fusion theorem
are valid with the hypotheses stated below. No claimed finite verification
package was available or replayed. No mathematical program was run.

## 1. Exact state convention

An ordered partition P=(B1|...|Bm) lists the coordinates already seen,
most recent last-occurrence class first. Its nonempty prefix unions are
exactly the distinct interval ORs ending at that endpoint. Appending a
nonempty letter X makes the update

\[
 T_X(P)=(X\mid B_1\setminus X\mid\cdots\mid B_m\setminus X),
\]

with empty blocks deleted. This is the exact move-to-front theorem in
`MASTER_HANDOFF.md`, Section 1.2. In particular, every legal edge entering
a prescribed nonempty state Q appends exactly the first block of Q.

## 2. General biclique and the edge cases

Let k,s,h,a be integers satisfying

\[
 0\le a<h\le s-2,\qquad g=k-s-h+a\ge1.
\]

Partition the k coordinates into disjoint sets H,C,D,G of sizes

\[
 |H|=h,\quad |C|=s-h-1,\quad |D|=h+1-a,\quad |G|=g.
\]

For every a-subset Y of H and every z in G put

\[
 \begin{aligned}
 P_Y&=(Y\mid C\mid D\mid H\setminus Y\mid G),\\
 X_z&=H\cup\{z\},\\
 Q_z&=(X_z\mid C\mid D\mid G\setminus\{z\}).
 \end{aligned}
\]

The exact transition is

\[
                         \boxed{T_{X_z}(P_Y)=Q_z.}       \tag{2.1}
\]

Indeed, subtracting X_z erases both Y and H\Y, leaves C and D, and
changes G to G\{z}; prepending X_z gives the displayed destination.
All quantities are actual physical sets, not only cardinality patterns.

There is a rank-s prefix in each source and each destination:

\[
 U_Y=Y\cup C\cup D,\qquad V_z=H\cup C\cup\{z\}.
\]

Their sizes are respectively a+(s-h-1)+(h+1-a)=s and
(h+1)+(s-h-1)=s. Distinct Y give distinct U_Y, and distinct z give
distinct V_z. No U_Y equals any V_z because U_Y contains the nonempty
set D whereas V_z is disjoint from D. Positive prefix increments make
this the unique rank-s prefix of each state.

Thus, choosing any

\[
                   q=\min\{\binom ha,g\}
\]

distinct sources and q distinct destinations gives q^2 legal cross edges
and 2q distinct rank-s prefix targets. Each edge appends a letter of
cardinality h+1. Its letter depends only on its destination.

The conditions ensure C is nonempty and |D|>=2. If a=0, the first source
block is empty and is simply deleted; q=1 and the same proof holds. If
g=1, the final destination block is empty and is deleted; again q=1 and
the same proof holds. Thus neither boundary case requires a zero letter
or an exception to the update rule.

## 3. The numerical k=17 gadget

Take s=9,h=4,a=2. Then |C|=4, |D|=3, g=6, and
binom(4,2)=6. The six P states and six Q states therefore have all
36 cross transitions, each appending a five-element letter H\cup{z}.
Their exact prefix-rank menus are

\[
 P_Y:\quad 2,6,9,11,17;\qquad
 Q_z:\quad 5,9,12,17.
\]

The six rank-nine U_Y and six rank-nine V_z are pairwise distinct by
the physical-set argument in Section 2. These counts follow from direct
algebra; they are not a claim that the user's enumeration was executed.

## 4. A growing family with small letters

Put r=floor(k/2), s=ceil(k/2), and choose the least nonnegative integer
a satisfying

\[
                         \binom{2a}{a}\ge r-a.           \tag{4.1}
\]

For r>=6 this choice is admissible with h=2a: in particular a>=1 and
2a<=r-2<=s-2. Here is an elementary finite check of admissibility.
For r=6,7 the trial a=2 works. For r>=8 set A=floor((r-2)/2)>=3.
Then 2A>=r-3>=r-A and binom(2A,A)>=2A, so (4.1) holds at A.
Minimality gives a<=A.

The resulting g is exactly r-a, so q=r-a. Also
binom(2a,a)>=2^a, since every factor (a+j)/j in its product is at least
two. Testing a=ceil(log_2 r) in (4.1) therefore proves

\[
 q\ge r-\lceil\log_2 r\rceil,
 \qquad |X_z|=2a+1\le2\lceil\log_2 r\rceil+1.
\]

Thus q=r-O(log k), and the appended letters have size O(log k).
The assertion about letter size is distinct from the number q^2 of
legal transitions. The family is valid for every k>=12; no claim about
the smaller inadmissible parameter choices is needed.

## 5. Coherent source-class fusion: exact hypotheses

Let V be a finite set of labelled state occurrences. Start with a directed
graph consisting of exactly one directed path, possibly a singleton,
and any number of directed cycles. Let i and t be the initial and terminal
vertices of the path. Its successor map is a bijection

\[
                       f:V\setminus\{t\}\longrightarrow V\setminus\{i\}.
\]

Partition all nonterminal source occurrences into nonempty classes C.
For each class, put D_C=f(C), and assume that every source in C has a
legal transition to every destination in D_C. Different occurrences may
carry the same state label; the combinatorial vertices remain distinct.

The permitted modification independently permutes the destination set
D_C among sources of C. Let G_aux be the undirected graph whose edges
are the original routing edges {v,f(v)} and all pairs of sources within
each class C. Let c be the initial component count and b the component
count of G_aux.

Then

\[
 \boxed{\text{The minimum attainable routing-component count is }b.}
                                                               \tag{5.1}
\]

Moreover b is attained by exactly c-b successor two-switches, all of
which merge two different current components. Classes may be processed
in any one fixed pass, using a reusable source anchor in each class.

The single-path hypothesis matters. With several disjoint paths, a
two-switch between paths generally exchanges suffixes and does not
merge components. For example, two paths P1->Q1 and P2->Q2 from a
two-source biclique have a connected auxiliary graph after adding the
class edge P1--P2. Nevertheless either successor permutation still has
two paths, because Q1 and Q2 remain distinct terminal vertices. The
theorem as stated makes no such multi-path claim.

## 6. Proof of the minimum and the one-pass construction

Every allowed new edge has the form u->f(v), with u and v in the same
original source class. Its endpoints lie in one auxiliary component:
follow the class edge u--v and then the old routing edge v--f(v).
Consequently no allowed routing component can cross an auxiliary
component, and every routing has at least b components.

Now take two sources u,v in one class but in different current routing
components. Swap their current successors:

\[
 u\to\alpha,\ v\to\beta
            \quad\longmapsto\quad u\to\beta,\ v\to\alpha.    \tag{6.1}
\]

The two new edges are legal because the current destinations of that
class still form exactly D_C. The switch preserves every indegree and
outdegree, and keeps i and t fixed. If both components are cycles, the
two opened cycles join into one cycle. If one is the distinguished path,
the cycle is inserted between its prefix through u and its suffix from
alpha. It becomes one path with the same initial and terminal vertices.
Thus (6.1) always merges the two components and never splits either.

For each class C, select one source anchor u. Whenever another source
of C is outside the anchor's current component, perform (6.1) with that
source. The anchor remains a source in the enlarged component and may
be reused. When this class is finished, all of its sources are connected.
Later operations only merge components, so they cannot undo that property.

After processing every class, every class-clique edge joins vertices in
one final component. Every original routing edge also has its endpoints
in one final component, because all operations only merged original
components. Therefore every auxiliary connected component is contained
in a final routing component. Combined with the lower bound, the two
component partitions are identical.

Each operation reduced the count by exactly one, so there were exactly
c-b operations. A successor two-switch cannot reduce the component count
by more than one, so this is also the smallest possible number of such
switches achieving b components.

## 7. Exactly what the rerouting preserves

The vertex multiset is unchanged. Therefore the complete multiset of
prefix targets carried by all labelled recency states is unchanged.
Every destination occurrence still receives exactly one incoming edge,
except the same initial occurrence i. Since any legal incoming edge
appends that destination's first block, the multiset of appended letters
is unchanged as well. Each class separately retains its destination
multiset, which is the coherence condition needed for repeated switches.

If b=1 and i is the empty recency state, the final graph is one legal
path from the empty state through every occurrence to t. Reading its
edge letters produces an ordinary word of exactly |V|-1 letters. The
move-to-front theorem makes every preserved prefix target a literal
interval OR of this word. This is exact preservation of the named target
inventory, not merely preservation of its rank counts.

If i is a prescribed nonempty state, initialization must already be part
of the original path or separately charged. If b>1, the remaining cycles
still require a separate construction step. One cannot infer an ordinary
word of unchanged length merely from a disconnected family of state cycles.

## 8. Application boundary

The biclique supplies a genuine coherent q-source menu whenever these
states occur in a legal routing with f(P_Y) equal to its selected Q states.
If its sources lie in q distinct current components, that one class can
merge those components using q-1 legal switches.

The local algebra does not construct an all-target state inventory, place
these states into the currently proposed k=17 source, or prove that its
global auxiliary graph is connected. Those are separate finite embedding
and coverage obligations. In particular, these results alone do not
improve the proved finite value bounds or establish nu(k)=B(k).
