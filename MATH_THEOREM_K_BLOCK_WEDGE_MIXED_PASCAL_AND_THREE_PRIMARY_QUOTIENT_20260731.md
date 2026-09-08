# Block-wedge common refinement and the three-primary Pascal quotient

Date: 2026-07-31  
Status: dimension-free constructive equivalence, exact obstruction to the
gain-closed GMM modification, exact quotient-lift reduction, and exact
global-quotient matching/filter reduction and multi-spiral opening ledger;
no all-\(m\) existence theorem

## 0. Verdict

The physical recursion state is a **path-wedge package**, not merely two
palette bijections. A two-sided-rainbow spanning \(K\)-path forest plus a
cyclic endpoint closure gives a cap-two \(P\)-respecting Hamilton cycle
exactly when every incoming connector repeats the upper colour of the first
forest edge at its target. Two further squarefree ledgers give the exact
lower floor and \(K\) directed repair ears.

The most tempting all-\(K\) modification of the published GMM one-port
splice is impossible. If its gain bank equals its direct-label bank, the
selected ports and labels induce a proper closed subcycle of the central
alternating Hamilton cycle. In every viable mixed bank,

\[
t=|X\setminus Y|=|Y\setminus X|\ge 1
\]

is exactly the number of selected alternating intervals. Precisely \(t\)
direct blocks need retained tagged-child partners; the other \(K-t\) get
automatic gain partners.

At the maximal clean cyclic scale

\[
h=\frac{2m-1}{3^{v_3(2m-1)}},
\]

an equivariant construction has \(K/h\) quotient repair blocks. The
symmetry closure of the one published GMM atom supplies at most one. When
compatible it leaves the exact quotient count deficit \(K/h-1\). If
\(3\mid(2m-1)\), the quotient data must have trivial stabilizer under the
residual 3-primary action.

The complete clean-\(H\) quotient diamond graph is balanced regular, so it
always has a global quotient perfect matching. Its restriction to every
exceptional bank is automatically extendable and supplies the minimal
valuation-one period-three filters with mutually distinct middle endpoints.
Thus residual-palette Hall is not the existential gate. The missing choice
is a global quotient matching whose **entire physical diamond lift** is a
spanning linear forest with the required wedges, private sockets and
voltage closure.

There is also a rigorously distinct linear branch. Co-oriented strict
spirals may interlace every residual sector; opening \(r\) such cycles and
adding \(r-1\) Johnson seams gives one physical path with an exact signed
lower/upper palette ledger. The K16 optimum realizes this with four
\(\mathbb Z_{15}\)-spirals of base lengths \(426,426,3,3\) and voltage
\(+4\). This does not by itself supply the protected repair ears, deeper
collars, or compiler, and the final compiler need not be equivariant.

The authenticated \(m=4\), \(\mathbb Z_7\)-equivariant fixture is a positive
block-wedge base: its quotient forest has paths of orders \(3\) and \(7\),
and its quotient closure has voltage \(2\). The newer varied-size
flag-matching forest is a strict negative fixture: it has a Johnson
Hamilton closure and complete immediate colour coverage, but its path
\(0x95-0xc5\) admits no incoming equal-union connector from another
component.

## 1. Dimension-free path-wedge theorem

Fix \(m\ge 2\), and put

\[
M=\binom{2m}{m},\qquad
N=\binom{2m}{m-1}=\binom{2m}{m+1},\qquad
K=M-N=\operatorname{Cat}_m.
\tag{1.1}
\]

For an edge \(ab\) of \(J(2m,m)\), write

\[
\ell(ab)=a\cap b,\qquad u(ab)=a\cup b.
\]

Let \(F\) be a spanning forest of \(K\) nontrivial paths whose \(N\)
edges use every rank-\((m-1)\) lower colour and every rank-\((m+1)\)
upper colour exactly once. Orient path \(i\) from tail \(t_i\) to head
\(h_i\), and let \(n_i\) be the neighbour of \(t_i\).

Let \(\sigma\) be a \(K\)-cycle and add the Johnson edges

\[
c_i=h_{\sigma^{-1}(i)}t_i.
\tag{1.2}
\]

Define

\[
\begin{aligned}
U_i&=t_i\cup n_i,\\
\alpha_i&=h_{\sigma^{-1}(i)}\cap t_i,\\
\beta_i&=t_i\cap n_i,\\
d_i&=h_{\sigma^{-1}(i)}\cap n_i.
\end{aligned}
\tag{1.3}
\]

### Theorem 1.1 (path-wedge equivalence)

The following statements hold.

1. \(F+\{c_i:i\in[K]\}\) is a Hamilton cycle.
2. Its two edges at \(t_i\) form a literal cap-two block if and only if
   \[
   h_{\sigma^{-1}(i)}\cup t_i=t_i\cup n_i=U_i.
   \tag{1.4}
   \]
   If (1.4) holds for all \(i\), the \(U_i\) are automatically distinct
   and the upper load profile is \(1^{N-K}2^K\).
3. The lower load profile of the full Hamilton cycle is
   \(1^{N-K}2^K\) if and only if the \(\alpha_i\) are distinct.
4. Under (1.4), suppressing every \(t_i\) gives an upper-rainbow saturating
   cycle on \(N\) middle states with lower multiset
   \[
   \mathbf 1_{\binom{[2m]}{m-1}}
   -\sum_i\mathbf1_{\beta_i}+\sum_i\mathbf1_{d_i}.
   \tag{1.5}
   \]
   It has profile \(0^K1^{N-2K}2^K\) if and only if the \(d_i\) are
   pairwise distinct and
   \[
   \{d_i:i\in[K]\}\cap\{\beta_i:i\in[K]\}=\varnothing.
   \tag{1.6}
   \]
5. Under (1.4), the literal expansion/cut at block \(i\) has repair ledger
   \[
   (t_i,d_i,\beta_i;U_i),
   \tag{1.7}
   \]
   with incoming cut colour \(\alpha_i\), and changes the lower multiset by
   \[
   -d_i+\alpha_i+\beta_i-\alpha_i=-d_i+\beta_i.
   \tag{1.8}
   \]
   These are \(K\) zero-slack repair ears exactly when the \(d_i\) are
   pairwise distinct and (1.6) holds.

Conversely, suppose a simple Hamilton cycle has \(K\) pairwise edge-disjoint
hosted cap-two blocks with distinct upper hosts and pairwise distinct
incoming occurrences, all with one cyclic sign, and cutting the incoming
edges leaves no isolated vertex. Let \(B\) be the lower multiset of the
suppressed cycle, and suppose

\[
B+\sum_i(-\mathbf1_{d_i}+\mathbf1_{\beta_i})
=\mathbf1_{\binom{[2m]}{m-1}},
\tag{1.9}
\]

while expansion and cutting preserve every upper colour exactly once.
Cutting those occurrences yields exactly the data above. If the full-cycle
lower floor is also required, the incoming colours \(\alpha_i\) must be
distinct.

#### Proof

Every endpoint receives one connector, and contraction of the paths gives
the cycle \(\sigma\), proving Hamiltonicity. Equation (1.4) is exactly the
equal-union condition for the connector and first forest edge. The first
forest edges have distinct upper colours because \(F\) is upper-rainbow.
The full lower ledger is the exact forest ledger plus the \(\alpha_i\),
proving statements 2 and 3.

Suppression removes both the connector colours and the first-edge colours,
then inserts the smoothed colours:

\[
\mathbf1+\sum_i\mathbf1_{\alpha_i}
-\sum_i\mathbf1_{\alpha_i}
-\sum_i\mathbf1_{\beta_i}
+\sum_i\mathbf1_{d_i}.
\]

This is (1.5). The \(\beta_i\) are already distinct. Hence pairwise
distinctness of the \(d_i\), together with (1.6), is exactly the extremal
floor condition. Equation (1.8) is the reverse expansion and cut. The
converse reverses these operations occurrence by occurrence. \(\square\)

The forest edges are a common lower/upper flag matching. Together with the
blockwise complementary occurrences, they give the established rigid
\(P\)-respecting lower/upper diamond enumeration. Distinct
\(\alpha_i\) are needed for the stronger squarefree complementary-cut
ledger, not merely for the selected common matching.

The theorem does not imply uniqueness of the common matching or
leaf-peelability of the full alternative-host repair atlas.

## 2. Exact obstruction inside the GMM square architecture

Put

\[
n=2m-1,\qquad k=m-1,\qquad
A=\binom nk,\qquad B=\binom n{k-1},\qquad K=A-B.
\tag{2.1}
\]

Let \(C_0\) be the alternating tight enumeration of old ranks \(k,k+1\).
For direct tagged-child edge \(r_is_i\), put \(x_i=r_i\cup s_i\).
Choose the central incidence \(r_i-x_i\), and let \(y_i\) be the other
neighbour of \(r_i\) on \(C_0\). The Pascal square is

\[
\{r_i0-x_i0,r_i1-s_i1\}
\longmapsto
\{r_i0-r_i1,x_i0-s_i1\}.
\tag{2.2}
\]

Let

\[
\mathcal P=\{r_i\},\qquad X=\{x_i\},\qquad Y=\{y_i\}.
\]

### Theorem 2.1 (closed alternating-subcycle obstruction)

If \(\mathcal P,X,Y\) are multiplicity-one \(K\)-banks and \(Y=X\), then
\(C_0[\mathcal P\cup X]\) is a nonempty closed two-regular subgraph.
Since \(C_0\) is one Hamilton cycle, this forces \(K=A\), contradicting
\(A=B+K\) and \(B>0\).

#### Proof

Every selected port has both neighbours \(x_i,y_i\) in \(X\). Conversely,
each \(x\in X\) occurs once as a selected neighbour and once as a gain, so
both of its neighbours lie in \(\mathcal P\). Thus the induced subgraph
has no boundary edge and is two-regular. A nonempty closed subgraph of one
cycle is the whole cycle, but \(K<A\). \(\square\)

### Theorem 2.2 (mixed interval law)

Let \(\mathcal P,X,Y\) each be a multiplicity-one bank of cardinality
\(K\), allowing \(X\) and \(Y\) to overlap. Put

\[
t=|X\setminus Y|=|Y\setminus X|.
\tag{2.3}
\]

Then \(C_0[\mathcal P\cup X]\) consists of exactly \(t\) balanced
alternating paths, and

\[
|V|=2K,\qquad |E|=2K-t,\qquad
|\delta_{C_0}(\mathcal P\cup X)|=2t.
\tag{2.4}
\]

In particular \(t\ge1\). If the retained tagged labels \(R\) and gains
form the exact palette

\[
R\mathbin{\dot\cup}Y=\binom{[n]}{k+1},
\tag{2.5}
\]

then the \(K-t\) labels in \(X\cap Y\) have gain partners, while the \(t\)
labels in \(X\setminus Y=X\cap R\) require retained partners.

#### Proof

The induced graph has the \(K\) selected matching edges and one further
edge for each gain in \(X\), namely \(K-t\) edges. It is a proper
subgraph of one cycle and hence a forest. Its selected perfect matching
makes every component a balanced path, and Euler's identity gives \(t\)
components. The endpoint and palette statements follow. \(\square\)

For gain partner \(y_j=x_i\), the block pivot is

\[
(X_i,d_i,h_i;U_i)
=\bigl(x_i,z+(r_j\cap s_i),r_j;z+x_i\bigr).
\tag{2.6}
\]

The degeneration \(r_j=s_i\) must be excluded. For retained partner
\(s_i1-c_i1\), literal contiguity holds exactly when the retained
occurrence is incident with \(s_i1\), and

\[
(X_i,d_i,h_i;U_i)
=\bigl(z+s_i,c_i,z+(s_i\cap c_i);z+x_i\bigr).
\tag{2.7}
\]

### Corollary 2.3 (correct mixed Pascal sufficient package)

An all-\(K\) square bank gives the block-wedge package of Theorem 1.1 if
all of the following hold:

1. the squares are pairwise compatible and edge-disjoint, with simple
   physical support, distinct ports, and distinct direct labels;
2. both sector palettes are exact;
3. the \(t\) retained incidences exist, and every gain partner is
   nondegenerate;
4. cutting the complementary direct occurrences leaves a spanning
   two-sided-rainbow \(K\)-path forest;
5. the fragment closure is connected and all blocks have one sign;
6. the selected hole bank \(\{h_i\}\) and pivot bank \(\{d_i\}\) are
   squarefree and satisfy
   \[
   \{d_i\}\cap\{h_i\}=\varnothing;
   \tag{2.8}
   \]
7. the incoming \(\alpha_i\) are distinct when the complementary lower
   floor is required.

The published theorem does not assert or control items 3--7.

In the parallel-oriented two-parent subfibre, the output components are
the cycles of \(\alpha^{-1}\beta\), where \(\alpha,\beta\) are the two
cyclic cut-successor permutations. This permutation is even. Hence a
connected parallel bank forces \(K\) odd. A twisted signed-port bank is
outside this parity obstruction.

## 3. Clean cyclic quotient and voltage lift

Put

\[
q=2m-1,\qquad s=3^{v_3(q)},\qquad h=q/s,
\tag{3.1}
\]

identify the ground set as
\(\Omega=\mathbb Z_q\sqcup\{\infty\}\), and let
\(H=\langle s\rangle\cong\mathbb Z_h\).

The identity

\[
(m^2-1)\operatorname{Cat}_m
=2(2m-1)\binom{2m-2}{m-2}
\tag{3.2}
\]

and \(\gcd(h,m^2-1)=1\) imply \(h\mid K\). The group \(H\) acts freely on
ranks \(m-1,m,m+1\): a set fixed by an element of order \(d>1\) dividing
\(h\) has finite part divisible by \(d\), whereas the possible finite-part
sizes \(m-2,m-1,m,m+1\) are all coprime to \(h\).

### Theorem 3.1 (equivariant block-wedge/voltage lift)

Suppose an \(H\)-invariant package has the following quotient data.

1. A spanning common-flag forest with exactly \(K/h\) path components,
   covering every lower- and upper-colour orbit once.
2. \(K/h\) connector orbits joining the path endpoints into one quotient
   cycle.
3. Simple physical support and one block sign.
4. The wedge equations and injective \(\alpha\)-orbit ledger.
5. Injective \(d\)- and \(\beta\)-orbit ledgers and the untyped separation
   \[
   \{d\}\cap\{\beta\}=\varnothing.
   \tag{3.3}
   \]
6. Total quotient-cycle voltage \(v\in\mathbb Z_h\).

Then the lift is a physical block-wedge package with \(K\) repair ears.
It is one Hamilton cycle exactly when

\[
\gcd(v,h)=1.
\tag{3.4}
\]

More generally it has \(\gcd(v,h)\) cycle components.

#### Proof

Freeness makes orbit matching exact. A voltage assignment on a quotient
path is gauged to zero, so each quotient path lifts to \(h\) disjoint
paths. The quotient conditions lift all identities of Theorem 1.1.
One quotient circuit translates the fibre by \(v\), whose action on
\(\mathbb Z_h\) has \(\gcd(v,h)\) orbits. \(\square\)

When \(3\mid q\), full \(\mathbb Z_q\)-equivariance is impossible. The
outer ranks contain colour orbits with stabilizer divisible by three,
whereas every Johnson-edge orbit is free. A full edge orbit therefore
hits each colour in such an orbit a multiple of three times, never once.
Consequently the full occurrence- and voltage-labelled quotient package
must have trivial stabilizer under the residual \(\mathbb Z_s\) action. Any
nonidentity residual stabilizer lifts to a forbidden symmetry group properly
containing \(H\) and divisible by three.

### Theorem 3.2 (co-oriented multi-spiral opening)

Let \(C_1,\ldots,C_r\) be vertex-disjoint cyclic blocks whose vertices
partition the desired carrier. In each \(C_j\), delete one oriented wrap
edge \(w_j=a_jb_j\), thereby obtaining a path from \(b_j\) to \(a_j\).
If

\[
a_jb_{j+1}\in E(J)\qquad(1\le j<r),
\tag{3.5}
\]

then adding these \(r-1\) seams gives one spanning Hamilton path. For any
edge-local label map \(\lambda\), in particular the immediate lower
intersection or upper union colour, the exact change is

\[
\Delta_\lambda
=-\sum_{j=1}^{r}\mathbf1_{\lambda(w_j)}
 +\sum_{j=1}^{r-1}\mathbf1_{\lambda(a_jb_{j+1})}.
\tag{3.6}
\]

Adding a final physical seam \(a_rb_1\) as well gives a cycle, with the
corresponding additional positive term in (3.6).

#### Proof

Deleting one edge from each cycle gives \(r\) disjoint spanning paths.
The seams in (3.5) concatenate them in order, so the result is connected,
has two endpoints, and every other vertex has degree two. Equation (3.6)
is the literal removed-edge/added-edge multiset identity. \(\square\)

When the \(C_j\) are strict cyclic voltage lifts, anchored reversal can
co-orient their voltage signs without changing their undirected internal
edge sets. Palette safety is not automatic: every unique label lost at a
wrap must be retained elsewhere or supplied by a seam. The theorem isolates
that exact opening ledger. Deeper shadows cross several edges and require
the separate finite collar/witness audit; (3.6) does not claim their
automatic preservation.

For the two immediate Johnson palettes, write \(L_0^-\) and \(L_0^+\)
for the lower-intersection and upper-union loads in the closed block bank,
and let \(\Delta^-\) and \(\Delta^+\) be (3.6) for those two label maps.
There are three distinct notions which must not be conflated:

1. the opening is **exact-palette-safe** when
   \(\Delta^-=\Delta^+=0\) as signed multisets;
2. it is **coverage-safe** when
   \(L_0^-+\Delta^-\ge1\) and \(L_0^++\Delta^+\ge1\)
   coordinatewise; and
3. it is **boundary-balanced** when the two signed changes equal a declared
   pair of boundary deficits which the downstream compiler explicitly
   absorbs.

The third form is the natural linear-carrier interface. Its two path
endpoints are physical resources, not an omitted quotient-voltage edge in
disguise.

Likewise, opening a wrap may touch a protected cap-two block. Every removed
wrap and every new seam must therefore either avoid the protected hosted
occurrences or trigger a fresh verification of the wedge equation and of
the \(\alpha,d,\beta\) ledgers. If \(e_{\rm int}\) old repair ears remain
untouched and \(e_{\partial}\) new or boundary ears are certified, the
output has exactly \(e_{\rm int}+e_{\partial}\) certified ears. No formula
involving only \(r\) or the seam count implies that this sum is \(K\).

This permits a second symmetry-breaking architecture besides one invariant
quotient cycle. The closed spiral factor may retain more symmetry, with all
residual sectors interlaced inside every block; a small set of physical
opening representatives can then destroy the forbidden residual stabilizer.
No separated-sector hypothesis is needed.

## 4. Test of the GMM atom and the period-three filters

The displayed GMM adjacent-level splice uses one physical Pascal square.
For \(h>1\) it is not \(H\)-invariant. Its smallest invariant closure is
its \(H\)-orbit.

### Corollary 4.1 (quotient count deficit)

An \(H\)-equivariant common refinement needs

\[
p=K/h
\tag{4.1}
\]

quotient hosted-block orbits. The orbit of the published atom supplies at
most one, so unconditionally the remaining count deficit is at least
\(p-1\). If all \(h\) conjugate squares are simultaneously compatible, it
supplies exactly one and the deficit is exactly

\[
p-1=K/h-1.
\tag{4.2}
\]

If the quotient parents are simple alternating cycles and the quotient
banks are multiplicity-one, Theorem 2.1 also descends: gain closure of
the \(p\) quotient ports is impossible. An invariant mixed construction
has

\[
\tau=t/h\ge1
\tag{4.3}
\]

retained-partner interval orbits.

### Theorem 4.2 (global quotient matching absorbs the filters)

Let \(\mathcal B_m\) be the lower--upper diamond graph with shores

\[
\binom{[2m]}{m-1},\qquad \binom{[2m]}{m+1},
\]

and adjacency by containment. It is balanced and
\(\binom{m+1}{2}\)-regular. Since \(H\) acts freely on both shores,
\(\mathcal B_m/H\) is a balanced regular bipartite multigraph. Hence it has
a perfect matching, and the union of the selected \(H\)-edge orbits is an
\(H\)-invariant physical perfect matching \(\mathcal M\) of
\(\mathcal B_m\).

Suppose \(q=6a+3\). Restrict \(\mathcal M\) to the exceptional lower and upper
banks. Then every exceptional colour is serviced exactly once, every used
opposite-shore colour is distinct within its physical shore, the lower and
upper filter families are disjoint, and all physical rank-\(m\) middle
endpoints of these filter diamonds are pairwise distinct. The restriction
is globally extendable by construction: its extension is \(\mathcal M\)
itself. No cross-shore distinctness after complement-identifying the two
shore label sets is asserted.

When \(v_3(q)=1\), this restriction consists of exactly

\[
2\operatorname{Cat}_a
\tag{4.4}
\]

clean-\(H\) edge orbits and attains the sharp partial-full-rotation-orbit
floor. At general 3-primary valuation it contains
\(2\operatorname{Cat}_a(s/3)\) clean-\(H\) edge orbits, one for every
exceptional quotient vertex. Thus compatibility of separate phase sections
and residual Kneser Hall are not independent existence gates.

#### Proof

Every quotient vertex has degree \(\binom{m+1}{2}\), counted with edge-orbit
multiplicity. Edge counting gives Hall in the quotient, and freeness lifts a
quotient perfect matching to a physical perfect matching. No diamond joins
the exceptional lower bank to the exceptional upper bank: after
complementing the upper shore, both exceptional types contain \(\infty\),
so they are not disjoint. The matching therefore uses one distinct edge for
each exceptional quotient vertex on each shore.

At valuation one there are \(\operatorname{Cat}_a\) exceptional quotient
vertices per shore. Each shortened full colour orbit has size
\(q/3=h=|H|\); since the \(H\)-action is free, it is transitive on that
orbit. Each selected clean edge orbit is therefore exactly one of the three
phases of its free full-rotation edge orbit; a second phase would rematch the
same exceptional quotient vertex. At higher valuation each shortened
full-rotation colour orbit splits into \(s/3\) clean-\(H\) orbits, giving the
displayed count.

Finally, two distinct exceptional colours on the same shore differ by whole
order-three cosets, so their symmetric difference has size at least six.
They cannot both lie below, or both lie above, one rank-\(m\) middle set.
Lower-filter middle endpoints contain \(\infty\), while upper-filter middle
endpoints avoid it. Hence all filter middle endpoints are distinct.
\(\square\)

The theorem changes the order of construction: choose a global quotient
perfect matching first and let its restriction define the filters. It does
not assert that every independently prescribed complement-paired filter
extends. Nor does pairwise distinctness inside the exceptional restriction
prevent a nonexceptional edge of \(\mathcal M\) from using one of those middle
vertices. The full physical diamond lift of \(\mathcal M\) may have arbitrary middle
degrees or cycles; the spanning-linear-forest condition remains separate.

### Lemma 4.3 (the global filters are Pascal-imbalance neutral)

Let

\[
A=\binom q{m-1},\qquad B=\binom q{m-2},\qquad A-B=K.
\]

Relative to \(\infty\), the lower shores have sizes \(A\) without
\(\infty\) and \(B\) with \(\infty\); the upper shores have sizes \(B\)
without \(\infty\) and \(A\) with \(\infty\). Let \(E\) be the number of
physical exceptional colours on either side. The lower-exceptional part of
the global matching matches \(E\) with-\(\infty\) lower colours to \(E\)
with-\(\infty\) upper colours. The upper-exceptional part uses \(E\)
without-\(\infty\) lower colours and \(E\) without-\(\infty\) upper colours.

After deleting these matched endpoints, the four shore sizes are

\[
(A-E,\ B-E;\ B-E,\ A-E).
\]

Every remaining without-\(\infty\) upper colour must be matched from the
without-\(\infty\) lower shore. Consequently exactly

\[
(A-E)-(B-E)=K
\tag{4.5}
\]

remaining lower colours must still cross to the with-\(\infty\) upper
shore. Thus the exceptional matching does not reduce the Catalan port
requirement. At the clean quotient scale it removes equal numbers from the
four quotient shores and leaves exactly \(K/h\) cross ports.

#### Proof

Containment forbids a lower colour containing \(\infty\) from lying below
an upper colour avoiding \(\infty\). Hence all \(B-E\) remaining
without-\(\infty\) upper colours consume \(B-E\) of the \(A-E\)
without-\(\infty\) lower colours. The displayed difference is forced, and
the same count is the residual capacity on the with-\(\infty\) upper shore.
\(\square\)

At every 3-primary valuation, Theorem 4.2 absorbs the phase choices and
their nonexceptional palette extension into one global quotient matching.
At higher valuation this is minimal in clean-\(H\) orbit count; it need not
use only \(2\operatorname{Cat}_a\) partial full-\(\mathbb Z_q\) edge-orbit
classes. The published GMM/BTK theorem still does not select a global
matching whose physical diamond lift is a spanning path forest with
protected wedges and voltage closure. Lemma 4.3 also shows that the
automatic filters do not rescue the one-port recursion: the old \(K-1\)
physical deficit, or conditional \(K/h-1\) quotient deficit, remains
unchanged.

The quotient sizes are:

\[
\begin{array}{c|c|c|c|c|c}
m&q&s&h&K&K/h\\ \hline
3&5&1&5&5&1\\
4&7&1&7&14&2\\
5&9&9&1&42&42\\
6&11&1&11&132&12\\
7&13&1&13&429&33\\
8&15&3&5&1430&286
\end{array}
\tag{4.6}
\]

This rules out propagation of the literal globally three-orbit \(m=4\)
core. It does not rule out a bounded recursive motif which generates a
growing number of orbit instances.

## 5. The two \(m=4\) fixtures

### 5.1 Positive cyclic fixture

For the authenticated uniformly outgoing fixture,

\[
q=h=7,\qquad s=1,\qquad K/h=2.
\]

Its two-sided-rainbow forest consists of two free path orbits: seven paths
of order \(3\) and seven paths of order \(7\). The quotient forest is two
paths on ten vertices. Two connector orbits make a quotient ten-cycle of
voltage \(2\), so its lift is the physical 70-cycle.

The complete repair core has three free edge orbits

\[
\mathcal E,\qquad\mathcal K_0,\qquad\mathcal K_1.
\]

The orbit \(\mathcal E\) is forced, while the residual quotient has the two
parallel choices \(\mathcal K_0,\mathcal K_1\). The two repair matchings
are

\[
\mathcal E\sqcup\mathcal K_0,\qquad
\mathcal E\sqcup\mathcal K_1.
\]

The canonical base--hole swaps are

\[
C_7(\pm1)\cup C_7(\pm3)=K_7\setminus C_7(\pm2).
\tag{5.1}
\]

This is the correct block-coherent cyclic base. What remains unknown is a
factorization of its quotient paths and repair orbits into two suitable GMM
parents satisfying Corollary 2.3.

### 5.2 Varied-size flag forest

The newer literal flag matching uses every rank-three and rank-five colour
once. Its unique Johnson lift is a spanning 14-path forest of orders

\[
21,7,7,6,5,5,4,3,2,2,2,2,2,2.
\tag{5.2}
\]

The displayed connectors give a Johnson Hamilton cycle and complete
immediate lower/upper coverage. They have only 13 distinct lower colours
and 12 distinct upper colours. The two cyclic orientations satisfy only
\(2/14\) and \(6/14\) wedge equations.

No alternative all-wedge endpoint closure exists for this fixed forest.
The path \(0x95-0xc5\) has first-edge upper colour \(0xd5\) in either
orientation. Among all 28 endpoints, the only \(0xd5\)-facets are
\(0x95,0xc5\), both on that path. Thus both oriented states have indegree
zero in the full equal-union compatibility digraph, which has 34 arcs.

This proves, for this fixed forest,

\[
\text{common transversal + Johnson Hamilton closure}
\not\Longrightarrow
\text{block-coherent cap-two repair}.
\]

## 6. K16 calibration of the multi-spiral alternative

The authenticated optimum carrier in dimension 16 is the concatenation of
four strict, co-oriented \(\mathbb Z_{15}\)-spirals with base lengths

\[
426,\qquad426,\qquad3,\qquad3
\]

and common sheet voltage \(+4\). Every spiral interlaces all three residual
\(\mathbb Z_{15}/\mathbb Z_5\) sectors. Closing the four blocks gives an
invariant four-cycle factor. Three physical Johnson seams concatenate their
openings into the linear carrier; the fourth cyclic wrap has symmetric
difference six and is deliberately absent.

This is exactly Theorem 3.2 with \(r=4\). It proves that the relevant
three-primary state is not “three separate sector packets.” It is a
co-oriented multi-spiral factor plus a palette-safe opening ledger.

The common-cap compiler may then be fully asymmetric. In the K16 fixture,
the vertex deck and the four closed spiral parametrizations are exactly
\(\mathbb Z_5\)-covariant. The physical opened path has \(12869\) Johnson
edges. If the deliberately absent non-Johnson wrap is adjoined solely for
the cyclic orbit audit, only \(12862\) of the resulting \(12870\) edge
entries are carried to selected entries by the clean generator; these are
the four literal phase defects. The decoded letter multiset is still less
symmetric. Thus no recursive common-refinement theorem may require
equivariance of the final integral compiler merely because the closed
carrier bank was built from quotient spirals.

## 7. Colour forest versus repair quotient

At a wedge block, with selected lower colour \(h\), complementary colour
\(\alpha\), and upper colour \(U\), the suppressed base is

\[
d=(h\cap\alpha)\cup\bigl(U\setminus(h\cup\alpha)\bigr).
\tag{7.1}
\]

The colour graph sees \(h-U\) and \(\alpha-U\); the repair graph sees
\(d-h\), labelled by the omitted middle facet. Leaf peeling does not
commute with this pivot.

The \(\mathbb Z_7\) fixture makes the distinction literal. Seven forced
ears leave a leafless cyclic kernel, but that kernel is one binary choice
after quotienting. This suggests carrying quotient matching and voltage
state rather than demanding individual-ear unitriangularity; it is not by
itself an induction theorem.

## 8. Exact remaining matching-forest lemma

The filters are no longer an input. The common core is:

> **Quotient matching forest \(\mathrm{QMF}(m)\).** Choose a perfect
> matching \(\overline{\mathcal M}\) of the complete quotient diamond graph
> \(\mathcal B_m/H\). Lift it to the physical matching \(\mathcal M\). Replace every
> matched diamond \(L\subset U\) by its unique Johnson edge between the two
> rank-\(m\) sets in \([L,U]\). Require the resulting graph
> \(F(\mathcal M)\) on all
> rank-\(m\) sets to be spanning, acyclic, and of degree one or two at every
> vertex.

The edge count is \(N=M-K\), so these conditions make
\(F(\mathcal M)\) a spanning
forest of exactly \(K\) nontrivial paths. Its lower and upper colours are
automatically exact because \(\mathcal M\) is a diamond perfect matching. By
Theorem 4.2 its exceptional restriction is also automatically the globally
extendable filter bank; at valuation one it has exactly
\(2\operatorname{Cat}_a\) clean-filter orbits. No residual-palette Hall
condition is part of \(\mathrm{QMF}(m)\).

There is an exact cycle-first form of the weaker common-transversal gate.
Let \(\overline C\) be one spanning occurrence cycle of the quotient
Johnson multigraph, and form the bipartite colour-incidence graph
\(G(\overline C)\) whose occurrence edges carry their lower and upper colour
orbits. Then

\[
G(\overline C)\text{ has a perfect matching}
\quad\Longleftrightarrow\quad
\overline C\text{ contains an exact quotient common transversal}.
\tag{8.1}
\]

The selected transversal is a proper edge subset of the cycle, hence a
linear forest with \(K/h\) quotient components, where isolated vertices are
counted as trivial paths. If the total voltage of \(\overline C\) is a unit
modulo \(h\), its physical lift is one Hamilton cycle. Conversely, every
clean-\(H\) Hamilton occurrence cycle containing an invariant exact common
transversal gives (8.1). Thus a coloured primitive-voltage quotient cycle is
an exact immediate-palette target. To enter the stronger block-wedge theorem
one must additionally exclude isolated selected vertices and verify the
wedge and pivot ledgers; (8.1) alone does not give repair ears.

Two different closure targets remain.

1. **Cyclic block-wedge closure.** Orient the \(K\) paths and choose an
   occurrence-private endpoint-socket cycle satisfying the wedge equations,
   simple support, one sign, injective \(\alpha,d,\beta\) ledgers and
   untyped \(d/\beta\) separation. In the quotient, require generating
   voltage. Theorems 1.1 and 3.1 then give a physical block-coherent common
   refinement with exactly \(K\) repair ears.
2. **Linear multi-spiral closure.** Organize the physical lift into finitely
   many co-oriented strict spirals with declared private openings, and
   concatenate them by a block path of occurrence-disjoint Johnson seams.
   Require (3.6) to be coverage-safe or equal to an explicit compiler
   boundary ledger; reverify every touched wedge and pivot; and exhibit the
   exact surviving internal/boundary ear count and deeper collars. Theorem
   3.2 gives only the path topology and immediate signed palette ledger. The
   downstream compiler may be fully asymmetric.

The mixed all-\(K\) GMM/Pascal square package of Corollary 2.3 is one
sufficient way to try to construct \(\mathrm{QMF}(m)\), not a necessary
normal form. Within that architecture Theorem 2.1 forces \(\tau\ge1\), and
Corollary 4.1 says the printed atom supplies at most one of the \(K/h\)
required quotient blocks. The new global matching theorem removes the
unconstrained colour-Hall problem, but it does not repair those additional
port, wedge, middle-degree, acyclicity or voltage constraints.

The \(m=4\) cyclic fixture verifies \(\mathrm{QMF}(4)\) and its cyclic
closure. Its decomposition into suitable GMM parents is not known. The
authenticated K16 anatomy verifies the topology and coverage-safe
immediate-palette part of the linear multi-spiral mechanism, not
\(\mathrm{QMF}(8)\). No coefficient-one or all-\(m\) existence claim is
made.

## 9. Frozen inputs

The decisive inputs are the gain-closed/mixed Pascal theorem and audit, the
colour-forest pivot theorem, the two \(\mathbb Z_7\) fixture theorems, the
three-primary quotient theorem, the period-three filter theorem, the global
quotient-matching theorem, and the two independent \(m=4\) replay packages
named in the research index.

The varied-size flag/connector certificate is self-contained through its
literal lists. Its transient producer file was observed and hashed but is
not currently present, so no producer-lineage claim is used.

The frozen finite and theorem anchors are:

* `MATH_THEOREM_K_GAIN_CLOSED_PASCAL_BLOCK_RECURSION_20260731.md`,
  SHA-256 `2290522c1318f1269fded06f458a5acf8d605607f635bf4937c9767e174a4cde`;
* `MATH_THEOREM_CATALAN_M4_Z7_QUOTIENT_REPAIR_CORE_20260731.md`,
  SHA-256 `ee0c5b3179e7abeee52d97a20d32b4424eb187e718d08e346ca743f09ee69649`;
* `MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`,
  SHA-256 `4d0614c5aadef320683dfd21196e5ee68d674faaeec954bcc2b6de73b6543b9a`;
* `MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md`,
  SHA-256 `0cc74f4610d2f13f443350c931fae3bd5377da817de821fb350ef9625a940ef9`;
* `MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md`,
  SHA-256 `a88042f078f76c369d20a353281dfc950abf634b624ce2bf80d2704c7e176d33`;
* `scratch/catalan_m4_flag_connector_lift_independent_20260731.audit.json`,
  SHA-256 `4ca7fbc04ebf8ce66fbbcc166b8fb33e80c6fbb73c9f721b86b3ee9813025608`;
  and
* `MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md`,
  SHA-256 `3367a823c8ebdd1b3c0d2b37422ea7fbe151f24bcfe47c0bb8c4c29a071b5c9a`.
