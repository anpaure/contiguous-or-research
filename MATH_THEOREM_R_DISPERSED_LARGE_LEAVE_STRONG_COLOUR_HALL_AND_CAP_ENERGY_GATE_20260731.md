# Dispersed large leaves: strong-colour Hall and the complete-ticket gate

Date: 2026-07-31  
Lane: R, all-parameter buffered C6 physicalization  
Status: exact conditional theorem and exact Catalan-scale counterexample.
No complete Pascal lift or additive-constant theorem is claimed.

## 1. Outcome

Let

\[
 \Omega=[2m-1],\qquad W_m=\binom{2m-1}{m}.
\]

A leave of size \(\Theta(W_m/m)\) is not intrinsically too large.  If its
task-to-incidence assignment has the weighted-code bounds

\[
 N_0^{\rm ext}=0,\qquad N_1=O(1),\qquad N_2=O(m),       \tag{1.1}
\]

then each token has external load \(O(m)\), irrespective of the number of
tasks.  Packets with \(O(d)\) tokens then have conflict degree \(O(md)\);
quadratic lists and Haxell work whenever \(d=o(m)\).

There is an explicit sufficient assignment mechanism.  Colour every
rank-\((m-1)\) anchor by its coordinate sum modulo a prime \(q>2m-1\).
A constant set of colours has both upper and lower multiplicity bounded by
that constant.  If the actual task graph restricted to those colours
satisfies Hall, then matching and a linear-size source-privacy pruning give
(1.1).

The restricted Hall row is essential.  An explicit task family of size
\(\Theta(W_m/m)\) forces

\[
 \max N_1=m-O(\log m)                                  \tag{1.2}
\]

under every injective facet assignment.  Thus the cardinality conclusion of
a DP physical-forest theorem does not by itself imply dispersion.

The theorem MATH_THEOREM_SPARSE_C6_AVERAGE_LOAD_EXTRACTION_20260731.md is
fully compatible with this obstruction: it chooses its own dispersed
anchors and obtains a raw reservoir of size at least
\(\widetilde W_m/(32m)\), where
\(\widetilde W_m=\binom{2m+1}{m}\).  Its tunable form in fact gives
\(\Theta(\widetilde W_m)\) compatible raw packets.
It does not cover a prescribed task leave.  Its extension to complete
witness and cap tickets requires a new full-ticket row-energy inequality;
a common cap-one cut vertex is an exact obstruction.

## 2. Literal incidence lists and weighted codes

Add new coordinates \(x,y\).  A task endpoint
\(R_i\in\binom{\Omega}{m}\) may use a facet
\(P\in\binom{R_i}{m-1}\) as the source incidence

\[
 e(P):\quad P+x\subset P+x+y.                          \tag{2.1}
\]

The standard incidence-C6 list at \(e(P)\) is indexed by

\[
 b\in P+x,\qquad c\in\Omega\setminus P
\]

and has exactly \(m^2\) choices.  A fixed typed token is source-fixed,
one-free, or zero-free, with multiplicity respectively

\[
                         m^2,\quad m,\quad1.           \tag{2.2}
\]

For an anchor family \(F\subseteq\binom{\Omega}{m-1}\), define

\[
\begin{aligned}
d_+^F(R)&=|\{P\in F:P\subset R\}|,\\
d_-^F(Q)&=|\{P\in F:Q\subset P\}|,\\
d_J^F(P')&=|\{P\in F:|P\cap P'|=m-2\}|.
\end{aligned}                                         \tag{2.3}
\]

Here \(R\) has rank \(m\), \(Q\) has rank \(m-2\), and \(P'\) has rank
\(m-1\).

### Lemma 2.1 (task-count-free token bound)

Suppose all selected source triples are private and

\[
 \max d_+,\max d_-\le A,\qquad \max d_J\le Bm.         \tag{2.4}
\]

Then every local physical, colour, or incidence token has external menu
load at most \((A+B)m\), up to the fixed role constants.  More generally,
assume every complete-ticket token has external load at most \(K_0hm\).
If every complete packet contains at most \(s_0d+s_1\) tokens, then

\[
                 \Delta\le K_0h(s_0d+s_1)m=O(md).      \tag{2.5}
\]

#### Proof

Source privacy removes the \(m^2N_0\) cross-list term.  The exact role table
then gives load \(mN_1+N_2\).  The one-free fibres are controlled by
\(d_+\) and \(d_-\).  Among the zero-free incidence roles, \(E_2\) is
controlled by \(d_-\), \(E_4\) by \(d_+\), and the two-coordinate swap
\(E_3\) by \(d_J\); the vertex roles have the same or smaller bounds.
Thus every zero-free fibre is at most \(Bm\), after absorbing fixed role
constants.  Union-bound the token neighbourhoods to obtain (2.5).
\(\square\)

The task count does not occur in (2.5).  This is what makes a dispersed
large leave logically possible.

## 3. Strong Johnson colouring and exact Hall

Choose a prime

\[
                         2m-1<q<4m,                   \tag{3.1}
\]

which exists by Bertrand's postulate, and define

\[
                 \chi(P)=\sum_{u\in P}u\pmod q.       \tag{3.2}
\]

### Lemma 3.1 (two-sided strong colouring)

The \(m\) facets of any rank-\(m\) set have pairwise distinct colours.
The rank-\((m-1)\) supersets of any fixed rank-\((m-2)\) set also have
pairwise distinct colours.

#### Proof

The facet \(R-u\) has colour \(\chi(R)-u\), and the superset \(Q+v\) has
colour \(\chi(Q)+v\).  Distinct coordinates remain distinct modulo
\(q>2m-1\). \(\square\)

Fix \(\Gamma\subseteq{\mathbb F}_q\), \(|\Gamma|=h\), and let

\[
 {\cal A}_\Gamma=\{P:\chi(P)\in\Gamma\}.               \tag{3.3}
\]

Every \(F\subseteq{\cal A}_\Gamma\) satisfies

\[
 d_+^F(R)\le h,\qquad d_-^F(Q)\le h,\qquad
 d_J^F(P')\le h(m-1).                                 \tag{3.4}
\]

The last inequality follows by summing over the \(m-1\) rank-\((m-2)\)
subsets of \(P'\).

For task \(i\), put

\[
 {\cal A}_\Gamma(i)=
 \{P\subset R_i:|P|=m-1,\ \chi(P)\in\Gamma\}.          \tag{3.5}
\]

### Theorem 3.2 (colour-selective Hall)

There is an injective assignment \(i\mapsto P_i\in{\cal A}_\Gamma(i)\)
if and only if

\[
 \left|\bigcup_{i\in J}{\cal A}_\Gamma(i)\right|
 \ge |J|\qquad(J\subseteq{\cal T}).                    \tag{3.6}
\]

Every such assignment satisfies (3.4).

#### Proof

Equation (3.6) is Hall's theorem in the restricted task--facet graph.
Lemma 3.1 proves (3.4) for every subset of the chosen colour classes.
\(\square\)

Thus edge-colouring reduces the weighted-code problem to ordinary Hall only
after a constant colour set satisfying (3.6) has been supplied.  It does
not create that set.

## 4. Source privacy costs only a linear slice

Distinct selected facets give distinct source incidences, but one selected
source can occur as a zero-free auxiliary triple in another list.

### Lemma 4.1 (deterministic source pruning)

For a matched anchor \(P_i\), delete every C6 whose nonsource support
contains the source incidence at another selected \(P_j\).  At most

\[
                         d_J^F(P_i)\le h(m-1)          \tag{4.1}
\]

choices are deleted, and all retained selected sources are private.

#### Proof

The source at \(P_j\) occurs in the list at \(P_i\) only if
\[
                       P_j=P_i-u+v.                   \tag{4.2}
\]
Then the unique parameters \((b,c)=(u,v)\) make the zero-free lower
vertex, upper vertex, and their incidence equal to the full source triple
at \(P_j\).  Hence there is one deletion per selected Johnson neighbour,
and (3.4) proves (4.1). \(\square\)

The suspended two-orientation list incurs at most the corresponding factor
two.

### Theorem 4.2 (dispersed large-leave selector)

Assume (3.6) for fixed \(h\), perform Lemma 4.1, and suppose all further
guards leave at least \(L_m\ge\alpha m^2\) complete packets per task.
Suppose also that every complete witness, cap and topology token has
external load at most \(K_0hm\).  Require at most a fixed number of
complete-ticket realizations per raw \((b,c)\) choice, absorbed into
\(K_0\); otherwise ticket multiplicity could amplify the raw role table.
Fix a backbone/slot
topology and private integral cap domains so that every pairwise-compatible
transversal satisfies the buffered global-composition theorem.  If every
packet has at most \(s_0d+s_1\) tokens, then one can choose one compatible
packet per task whenever

\[
                   L_m\ge2K_0h(s_0d+s_1)m.            \tag{4.3}
\]

For fixed constants and \(d=o(m)\), this holds eventually even for
\(|{\cal T}|=\Theta(W_m/m)\).

#### Proof

Equations (3.4) and (4.1) give source privacy, \(N_1\le h\), and
\(N_2\le h(m-1)\).  Lemma 2.1 bounds the maximum conflict degree by the
right side of (4.3) divided by two.  Haxell's independent-transversal
theorem applies. \(\square\)

The complete-ticket and fixed-composition premises are substantive.  The
local C6 table proves neither a low-load nonlocal compiler linkage nor the
absence of a higher-order graphic cycle.

## 5. Catalan-scale counterexample

For sufficiently large \(m\), put

\[
t=\left\lceil\log_2{m+1\over2}\right\rceil,\qquad
s=m-1-t,
\]

choose \(W\subset\Omega\) with

\[
                         |W|=2m-1-t=m+s,              \tag{5.1}
\]

and take every \(R\in\binom Wm\) as a task.

### Lemma 5.1 (exact scale)

If \(T_m=\binom{|W|}{m}\), then

\[
{T_m\over W_m}
=2^{-t}\prod_{j=0}^{t-1}
\left(1-{j+1\over2m-1-j}\right)
=\Theta(m^{-1}).                                      \tag{5.2}
\]

#### Proof

Cancelling factorials gives the product.  The second factor is
\(1-O(t^2/m)\), using
\(\prod(1-u_j)\ge1-\sum u_j\), while
\[
                 {1\over m+1}<2^{-t}\le{2\over m+1}.
\]
This proves (5.2). \(\square\)

Ordinary facet Hall nevertheless holds.  The task--facet graph is
biregular with left degree \(m\) and right degree \(s+1\le m\), so edge
counting gives \(|N(J)|\ge|J|\).

### Theorem 5.2 (forced concentration)

For every injective assignment
\[
 R\longmapsto P_R\subset R,\qquad |P_R|=m-1,
\]
put
\[
d_{\rm ext}(R')=
|\{R:P_R\subset R',\ R\ne R'\}|.
\]
Then
\[
\sum_{R'}d_{\rm ext}(R')=sT_m,\qquad
\max_{R'}d_{\rm ext}(R')\ge s=m-O(\log m).             \tag{5.3}
\]
Consequently one raw incidence-C6 token has external load at least
\(ms=\Omega(m^2)\), and the suspended two-orientation version has load at
least \(2ms\).  In particular \(N_1=O(1)\) is impossible.

#### Proof

Every selected \(P_R\subset W\) lies in exactly \(s+1\) task endpoints.
One is \(R\), so it contributes to exactly \(s\) terms in the sum.
This proves (5.3).  If \(P_R\subset R'\), the one-free upper role
\(C+c=R'+x\) occurs in all \(m\) choices of the other C6 parameter.
Removing the current list leaves at least \(m d_{\rm ext}(R')\) external
occurrences.  The suspended multiplicity is \(2m\). \(\square\)

This also proves that no constant \(\Gamma\) can satisfy (3.6) for this
task family.  Otherwise (3.4) would contradict (5.3).

The example does not assert that the DP leave is concentrated.  It proves
that its size alone cannot certify the large-leave route.

## 6. Pairwise exclusions do not replace a global code

Let \(L=m^2\), take \(L+1\) task parts each labelled by \([L]\), and make
equal labels conflict.  Each candidate excludes exactly one option in each
other list, yet a transversal would require \(L+1\) distinct labels and is
impossible.  The equal-label token has global \(N_2=L+1\).

Thus a per-pair \(O(md)\) exclusion estimate is useless when summed over a
large leave unless a global code, a direct maximum-degree bound, or an
average-pruning theorem controls the total.

## 7. Reconciliation with the sparse raw reservoir

Put \(\widetilde W_m=\binom{2m+1}{m}\).  The independently audited
sparse-C6 theorem chooses an endpoint-disjoint anchor family \(A\)
satisfying

\[
 |A|\ge{\widetilde W_m\over32m},\qquad
\text{average external packet degree in each list}\le16m.       \tag{7.1}
\]

Deleting candidates of degree greater than \(32m\) retains at least half
of every \(m^2\) list.  Haxell applies for
\[
                         {m^2\over2}\ge64m,
\]
namely \(m\ge128\).

More strongly, the exact raw row energy is

\[
 R_m=18m^3+51m^2-4m-5<44m^3.                         \tag{7.2}
\]

Sampling at \(p=1/(1408m)\), deleting anchor weighted degree above
\(4pR_m\), and pruning packet degree above \(8pR_m\) gives at least

\[
                   {3\widetilde W_m(m+1)\over5632m}
                   \ge {3\widetilde W_m\over5632}      \tag{7.3}
\]

compatible raw packets.  Thus raw supply is actually central-binomial
scale, well above the required Pascal leave scale.

This is complementary to Theorem 4.2:

1. the sparse theorem chooses its own anchors and need not cover a
   prescribed task family;
2. it tolerates high token loads by average pruning, while Theorem 4.2
   imposes a pointwise weighted code; and
3. it proves that Catalan-scale dispersed raw reservoirs exist, not that
   every Catalan-scale leave embeds in one.

Hence the raw local supply obstruction is closed.  The target-specific row
is (3.6), or an equally strong task-to-reservoir matching theorem.

## 8. Complete-ticket extension

Let \(E_0\) be an eligible anchor bank and let \({\cal Q}_e\) be a list of
\(L\ge\alpha m^2\) complete packets at every \(e\in E_0\), including every
protected witness, topology route and common-cap ticket.  Define

\[
{\cal E}(e,f)={1\over L}
|\{(p,q)\in{\cal Q}_e\times{\cal Q}_f:p\sim q\}|.       \tag{8.1}
\]

### Theorem 8.1 (tunable full-energy extraction)

Assume first that the lists use one fixed/triangular topology skeleton,
owned occurrence halos, and private/preallocated integral cap domains, so
that every independent transversal is a literal global composition.  If
\[
\sum_{f\in E_0-\{e\}}{\cal E}(e,f)\le K D_m m^3
\qquad\text{for every }e\in E_0,                       \tag{8.2}
\]
then take

\[
        p=\min\left\{1,{\alpha\over64KD_m m}\right\}.             \tag{8.3}
\]

Bernoulli anchor extraction at density \(p\), deletion of high-average
lists, per-list degree pruning, and Haxell produce

\[
                         \Omega(\widetilde W_m/D_m)     \tag{8.4}
\]

compatible complete packets in the nontrivial branch of (8.3), when
\(E_0\) is the full atlas.  For a restricted bank the exact conclusion is

\[
                         \Omega(|E_0|/(D_m m)).         \tag{8.4a}
\]

In particular \(D_m=\Theta(m)\) still gives Catalan-scale full-atlas
supply, but does not manufacture the special vertical Pascal anchors.

#### Proof

For any density \(p\), Markov deletion above weighted degree \(4pR_{\rm
full}\) retains at least \(3pI/4\) anchors whose lists have average
external degree at most \(4pR_{\rm full}\).  Pruning packet degree above
\(8pR_{\rm full}\) retains at least half of every list.  Haxell requires

\[
                    L_{\min}\ge32pR_{\rm full}.        \tag{8.5}
\]

With \(L_{\min}\ge\alpha m^2\), (8.2) and the choice (8.3) give
\(32pR_{\rm full}\le\alpha m^2/2\).  Finally
\(I=\widetilde W_m(m+1)\), so \(pI=\Omega(\widetilde W_m/D_m)\) for the
full atlas; replacing \(I\) by \(|E_0|\) gives (8.4a).
\(\square\)

The raw incidence calculation verifies (8.2) with \(D_m=1\).  No current
Pascal compiler theorem verifies it for complete cap and witness tickets.
Without the fixed-composition premise, three pairwise compatible connectors
may form a cycle, and three pairwise cap-feasible packets may compete for
two cells; neither obstruction is represented by the pair-conflict energy.

### Proposition 8.2 (cap cut-vertex obstruction)

Suppose \(M\) anchors have quadratic complete lists and every packet uses a
common cap-one vertex \(z\).  Then no compatible family contains two
packets, the cap gammoid has rank one on those tasks, and
\[
                         {\cal E}(e,f)\ge L
\qquad(e\ne f).                                       \tag{8.6}
\]
Thus the row contribution \((M-1)L\) forces
\[
                    D_m\ge{(M-1)L\over K m^3}.         \tag{8.7}
\]
At Catalan \(M\), this excludes the useful \(D_m=O(m)\), and indeed every
polynomial-energy regime.  It is not a contradiction if \(D_m\) is allowed
to be an arbitrarily large formal parameter.

#### Proof

Any two tickets meet at \(z\).  Menger gives linkage rank one.  All \(L^2\)
ordered packet pairs between two lists conflict; dividing by \(L\) proves
(8.6). \(\square\)

Read-only shared certificates are not conflict tokens, but that semantic
exception must be proved by the physical composition theorem.

## 9. Fixed-unused-bank compiler interface

Let \(H=(L,C;E_H)\) be one trace-guarded compiler graph containing every
final old and newborn compiler target, and fix a matching \(M_0\)
saturating every target in \(L\).  Its unused-cell bank is

\[
                         B=C-\operatorname{cells}(M_0).          \tag{9.1}
\]

For every packet task \(i\), let \(D_i\subseteq C\) be the cells at which
its compiler deletion may be placed.

### Theorem 9.1 (fixed-unused compiler elimination)

Assume

\[
 \left|\bigcup_{i\in J}(D_i\cap B)\right|\ge|J|
                       \qquad(J\subseteq{\cal T}).                \tag{9.2}
\]

Then one may fix distinct cells \(b_i\in D_i\cap B\).  Deleting all \(b_i\)
leaves the same matching \(M_0\) unchanged.  Suppose additionally that the
packet interface is globally Cartesian and frozen: every simultaneous
tuple of retained local packets changes the fixed graph \(H\) only by
deleting its assigned \(b_i\); it changes no target neighbourhood or trace
guard, and no packet touches another task's assigned cell.  Then the only
compiler token carried by task \(i\) is its private label \(b_i\).  Its
external compiler load is zero, and no cap path or rerouting ticket is
needed.

#### Proof

Hall's theorem applied to (9.2) gives distinct representatives \(b_i\).
No \(b_i\) is used by \(M_0\), so deleting all of them does not remove an
edge of \(M_0\).  Distinctness makes the fixed cell token private across
task lists.  Cartesian legality lets one choose the local C6 option later
without changing the cell. \(\square\)

This is the fixed-basis face of the compiler dual-Rado theorem.  For a
general deletion bank, dual independence guarantees that some saturating
matching survives; the fixed-unused face is stronger and is exactly what
turns the global cap row into private labels before Haxell.

### Corollary 9.2 (recomputed raw weighted load)

Under colour-selective Hall with \(|\Gamma|=h\), source pruning, and
Theorem 9.1, the raw list at every task retains at least

\[
                         m^2-h(m-1)                   \tag{9.3}
\]

choices.  A raw C6 has nine nonsource vertex/incidence tokens.  Every one
has external menu load at most \(hm\), while the fixed unused-cell token
has external load zero.  Hence

\[
                         \Delta_{\rm raw}\le9hm.       \tag{9.4}
\]

Haxell therefore gives one pairwise token-disjoint raw C6 per task whenever

\[
                     m^2-h(m-1)\ge18hm.               \tag{9.5}
\]

The simple sufficient threshold is \(m\ge19h\).

#### Proof

Equation (9.3) is Lemma 4.1.  There are two nonsource lower vertices, two
nonsource upper vertices, and five nonsource incidences.  Vertex roles
cannot cross between one-free and zero-free anchors because their
\(y\)-bits differ.  The incidence \(E_3\) is likewise isolated by its
\(y\)-pattern.  An incidence in roles \(E_1/E_2\), or symmetrically
\(E_4/E_5\), may cross roles: its one-free anchor and all its zero-free
anchors lie in one strong-colour-bounded facet/superset family.  After
excluding the packet's own list, their combined load is at most
\(m+h-2\le hm\) for \(m\ge2,h\ge1\).  Thus each of the nine actual typed
tokens, not merely each role, has external load at most \(hm\).
Union-bound their neighbourhoods to get (9.4), then apply Haxell.  At
\(m=19h\), the left side of (9.5) exceeds the right side by \(h\).
\(\square\)

This corollary certifies a raw local switch bank only.  A path/forest output
still requires the fixed topology composition row, and protected upper
witnesses must either be transported read-only or enter the weighted load.

For a bounded bank of \(H\) compound tasks, if one completed local packet
excludes at most \(\beta_{\rm loc}md\) choices in any other list, counting
every remaining physical, witness and topology conflict, the same interface
gives the sufficient greedy row

\[
                    L_m>(H-1)\beta_{\rm loc}md,        \tag{9.6}
\]

with no compiler term.  For an extensive leave, use (9.4) or the general
global weighted code rather than summing (9.6) over all tasks.

### Proposition 9.3 (separate marginal Hall is insufficient)

If allowed unused cells depend on the selected anchor or local packet,
separate anchor Hall and unused-cell Hall do not suffice.  With two tasks,
two anchors \(a_1,a_2\), and two unused cells \(b_1,b_2\), let

\[
\begin{aligned}
{\cal O}_1&=\{(a_1,b_1),(a_2,b_2)\},\\
{\cal O}_2&=\{(a_1,b_2),(a_2,b_1)\}.
\end{aligned}                                         \tag{9.7}
\]

Both projections are complete \(K_{2,2}\) Hall systems.  Nevertheless any
choice of one pair from each row repeats either its anchor or its cell.
Thus no joint assignment exists.  Cartesianity itself is not necessary:
many non-Cartesian option systems have a valid joint matching.  The example
proves only that a joint option condition is necessary for the inference.

The exact non-Cartesian object is a matching in the three-partite
task--anchor--unused-cell hypergraph, not two independent bipartite
matchings.  Equivalently, one must prove a joint dual-Rado/anchor theorem
for the actual option relation.

### Corollary 9.4 (effect on sparse full-ticket energy)

On the globally Cartesian frozen face of Theorem 9.1, treat \(M_0\) as a
read-only shared certificate.  The cap-path/compiler contribution to the
complete row energy (8.2) is then exactly zero, and the full row reduces to

\[
 R_{\rm full}=R_{\rm physical/colour}
              +R_{\rm protected\ witness}
              +R_{\rm topology}.                     \tag{9.8}
\]

If packet choices alter target neighbourhoods, introduce targets absent
from \(H\), or perturb trace guarding, this reduction is invalid.  Under
the frozen interface, if protected witnesses are transported read-only and
topology is fixed by a slot skeleton, the raw value \(R_m\) is sufficient for the compiler-
decorated packets.  What remains unproved for a Pascal child is precisely:

1. the joint or Cartesian task--anchor--unused-cell interface;
2. arbitrary-width witness transport for every option; and
3. one fixed global topology composition skeleton.

The cap cut-vertex obstruction of Proposition 8.2 is therefore bypassed,
not contradicted: it applies to path-routed cap tickets, while Theorem 9.1
uses cells already outside one trace-guarded matching.

## 10. Exact remaining theorem

The dispersed route bypasses absolute sparse exposure if a Pascal/DP lift
proves either:

1. a constant strong-colour set satisfying (3.6), a Cartesian fixed-unused
   bank satisfying (9.2), and weighted codes for only the remaining
   physical/witness/topology tokens; or
2. a task-covering form of sparse extraction satisfying the reduced full
   energy inequality (9.8), together with a fixed composition skeleton.

Raw Catalan-scale C6 supply and ordinary facet Hall are proved.  They do not
imply either target-specific statement.  The compiler path-ticket gate is
removed on the fixed-unused face; the sharp missing object is now a
dispersed task-to-anchor-to-unused-cell embedding with protected witness and
topology control, not merely a leave-cardinality bound.
