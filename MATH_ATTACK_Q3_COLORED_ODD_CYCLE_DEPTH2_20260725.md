# Colored odd-graph cycles through depth two

## Exact duality, deterministic literalization, and two nonpropagation theorems

## 1. Main verdict

Put

\[
n=2m+1,
\qquad
W=\binom nm,
\qquad
B=\frac Wn,
\qquad
N_q=\binom n{m-q}.
\]

For an oriented cyclic order \(\pi\), write \(I_\pi(j,r)\) for its cyclic
length-\(r\) interval starting at \(j\). If \(\mathcal F\) is an exact
middle wreath factor, define the lower depth-\(q\) multiset and its support
defect by

\[
\mathcal L_q(\mathcal F)
=\{I_\pi(j,m-q):\pi\in\mathcal F,\ j\in\mathbb Z_n\},
\]

\[
H_q(\mathcal F)
=N_q-|\operatorname{supp}\mathcal L_q(\mathcal F)|.
\tag{1.1}
\]

Thus \(H_0=0\). The new depth-two conclusions are as follows.

1. **Exact upper/lower duality.** Upper depth one is perfect, and the
   upper-depth-two multiplicity profile is exactly the complemented
   lower-depth-one profile. Hence lower depth two is the only new support
   gate after depth-one success.

2. **Deterministic cycle-to-word theorem.** Every exact factor produces a
   contiguous-OR word for ranks \(m-2,\ldots,m+2\) of length

   \[
   W+4B+2H_1+H_2.
   \tag{1.2}
   \]

   A complement-closed six-rank band through rank \(m+3\) has length

   \[
   W+5B+2H_1+2H_2.
   \tag{1.3}
   \]

3. **Exact conflict-free reduction.** The asymptotic statement

   \[
   \exists\ \mathcal F_m\text{ exact such that }
   H_1(\mathcal F_m)+H_2(\mathcal F_m)=o(W)
   \tag{D2WF}
   \]

   is equivalent to the existence inside the same exact factor of a
   vertex-disjoint path family covering \(W-o(W)\) middle vertices, having
   \(o(W)\) components, and having pairwise distinct lower and upper colors
   separately through depth two.

4. **True-wreath nonpropagation.** At every fixed depth \(h\), on an
   infinite sequence of dimensions there are two vertex-disjoint genuine
   wreath cycles whose lower colors are mutually disjoint through depth
   \(h-1\), whose upper colors are mutually disjoint through depth \(h\),
   but which share exactly \(n/(2h+1)\) lower depth-\(h\) colors. The
   collision family is itself a \(1\)-design, and eliminating the collisions
   while retaining the old transitions requires changing at least
   \(n/(2h+1)\) transitions.

5. **Near-spanning Johnson-cycle-packing counterexample.** There are
   near-spanning vertex-disjoint Johnson cycle packings whose depth-one
   lower colors and upper colors are globally conflict-free and miss only
   an asymptotically negligible number of targets, but whose lower
   depth-two support is itself asymptotically negligible. Thus
   even near-spanning two-sided cycle rainbowness does not imply depth-two
   success without the special wreath geometry and one-factor coupling.

6. **The proved Greene--Kleitman forest cannot be sparsely lifted.** Its
   rank-\((m-1)\) projection contains \((1/4+o(1))W\) branching labels.
   The duplicate-label slack in an exact factor is only \(o(W)\), forcing
   at least \((1/8-o(1))W\) edge replacements before that particular
   forest can lie in a degree-two occurrence graph.

Items 4--6 disprove local, componentwise, and black-box forest bootstraps.
They do **not** refute (D2WF), because neither counterexample is proved
extendible to one spanning exact wreath factor. Thus (D2WF) is the exact
remaining depth-two factor theorem.

## 2. Exact depth-two duality inside a wreath factor

For one oriented wreath put

\[
T_j=I_\pi(j,m),
\qquad j\in\mathbb Z_n.
\]

For \(0\le q\le m-1\), cyclic interval geometry gives

\[
\bigcap_{a=0}^{q}T_{j+a}
=I_\pi(j+q,m-q),
\tag{2.1}
\]

and

\[
\bigcup_{a=0}^{q}T_{j+a}
=I_\pi(j,m+q).
\tag{2.2}
\]

Let \(\mathcal U_q\) be the multiset in (2.2), aggregated over the exact
factor. Since \(n=2m+1\),

\[
[n]\setminus I_\pi(j,m+q)
=I_\pi(j+m+q,m+1-q).
\tag{2.3}
\]

The shift in \(j\) is a rowwise bijection. Therefore (2.3) proves the
multiset identity

\[
\boxed{
\{[n]\setminus U:U\in\mathcal U_q\}
=\mathcal L_{q-1}}
\qquad(q\ge1).
\tag{2.4}
\]

For \(q=1\), the right side is the exact middle layer, so every upper
depth-one color occurs exactly once. For \(q=2\), the upper profile is the
complement of \(\mathcal L_1\), including every multiplicity. In
particular,

\[
\boxed{
\text{upper-depth-two support defect}=H_1.}
\tag{2.5}
\]

Thus depth-one lower success automatically propagates to the upper half of
depth two. No identity relates \(\mathcal L_2\) to \(\mathcal L_1\); that is
the genuinely new gate.

## 3. Intact-cycle erosion gives a literal OR word

For integers \(a\le b\), let \(L_{[a,b]}\) denote the minimum length of a
word of subsets of \([n]\) whose contiguous unions include every set having
rank in \([a,b]\). Missing targets may always be appended as single literal
entries.

### Theorem 3.1 (general intact-cycle conversion)

Let \(1\le h\le m-1\), and let \(\mathcal P\) be a family of \(p\) directed
cyclic orders. Put

\[
M_q
=N_q-
\left|
\bigcup_{\pi\in\mathcal P}
\{I_\pi(j,m-q):j\in\mathbb Z_n\}
\right|
\qquad(0\le q\le h).
\tag{3.1}
\]

Then

\[
\boxed{
L_{[m-h,m+h]}
\le
p(n+2h)+M_h+2\sum_{q=0}^{h-1}M_q.}
\tag{3.2}
\]

If the first \(2h+1\) entries rather than the first \(2h\) entries are
repeated, then

\[
\boxed{
L_{[m-h,m+h+1]}
\le
p(n+2h+1)+2\sum_{q=0}^{h}M_q.}
\tag{3.3}
\]

#### Proof

For one order define

\[
E_j=I_\pi(j,m-h),
\qquad 0\le j<n.
\]

Emit

\[
E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2h-1}.
\tag{3.4}
\]

The copied prefix makes every cyclic start literal. For every
\(1\le t\le2h+1\),

\[
E_j\cup E_{j+1}\cup\cdots\cup E_{j+t-1}
=I_\pi(j,m-h+t-1).
\tag{3.5}
\]

The lower ranks \(m-h,\ldots,m\) have defects
\(M_h,M_{h-1},\ldots,M_0\). By complementation (2.3), the upper ranks
\(m+1,\ldots,m+h\) have defects \(M_0,M_1,\ldots,M_{h-1}\). The total
number of missing literals is therefore

\[
M_h+2\sum_{q=0}^{h-1}M_q.
\]

The emitted blocks cost \(p(n+2h)\), proving (3.2). Repeating \(E_{2h}\)
also makes \(t=2h+2\) available. Rank \(m+h+1\) then has defect \(M_h\),
which proves (3.3). No witness crossing two different cyclic blocks is
credited. \(\square\)

### Corollary 3.2 (depth two in one exact factor)

For an exact factor, \(p=B=W/n\) and \(M_0=0\). Taking \(h=2\) gives

\[
\boxed{
L_{[m-2,m+2]}
\le W+4B+2H_1+H_2,}
\tag{3.6}
\]

and

\[
\boxed{
L_{[m-2,m+3]}
\le W+5B+2H_1+2H_2.}
\tag{3.7}
\]

Appending every outer target literally gives the full, unconditional word
bound

\[
\boxed{
\nu(n)
\le
W+5B+2H_1+2H_2
+2\sum_{r=0}^{m-3}\binom nr-1.}
\tag{3.8}
\]

The subtraction removes the empty target, which is not required in the
nonzero-word convention. Equation (3.8) is an exact full OR-word
conversion, but its literal outer tail is not \(o(W)\) at fixed depth two.
What (3.6)--(3.7) prove sharply is that (D2WF) already finishes the entire
five- or six-rank central band at length \(W+o(W)\).

For comparison, cutting an otherwise depth-two-rainbow cycle and refusing
to credit crossing windows loses ten distinct five-band masks per cycle.
The intact construction copies only four entries. In general symmetric
depth \(h\), a raw cut loses

\[
\sum_{t=1}^{2h+1}(t-1)=h(2h+1)
\]

cyclic windows, whereas (3.4) costs \(2h\) copied entries. This is why the
cycle should be literalized intact rather than cut first.

### Corollary 3.3 (support and overload agree at depths one and two)

For \(m\ge8\), one has \(c_1=c_2=1\). If

\[
r_q=W-N_q,
\qquad
t_q=|\{S:\mu_q(S)\ge2\}|,
\]

then the exact overload identity is

\[
O_q=H_q+(r_q-t_q)_+.
\tag{3.9}
\]

Since \(r_1,r_2=O(W/m)\),

\[
H_q\le O_q\le H_q+O(W/m)
\qquad(q=1,2).
\tag{3.10}
\]

Consequently (D2WF) is equivalent to \(O_1+O_2=o(W)\).

## 4. The exact near-spanning conflict-free formulation

Put

\[
E_q=W-|\operatorname{supp}\mathcal L_q|
=(W-N_q)+H_q
\qquad(q=1,2).
\tag{4.1}
\]

### Theorem 4.1 (path-subfactor equivalence)

A sequence of exact factors \(\mathcal F_m\) satisfies
\(H_1(\mathcal F_m)+H_2(\mathcal F_m)=o(W)\) if and only if the disjoint
union of its reindexed Johnson cycles contains path subfactors
\(\mathcal P_m\) with all of the following properties. Every component of
\(\mathcal P_m\) is a contiguous factor subpath and every retained
transition is a factor transition.

1. \(\mathcal P_m\) uses \(W-o(W)\) middle occurrence vertices;
2. \(\mathcal P_m\) has \(o(W)\) path components, counting isolated vertices;
3. its lower and upper colors at depths one and two are pairwise distinct
   separately.

#### Proof

Suppress the subscript \(m\).

Suppose first that \(H_1+H_2=o(W)\). For every distinct lower depth-one
color, retain one occurrence and mark all other occurrences; there are
exactly \(E_1\) marked depth-one windows. Do the same at lower depth two,
marking \(E_2\) windows. By (2.4), the upper-depth-two duplicate excess is
also \(E_1\); upper depth one is already exact.

Delete every middle occurrence vertex lying in a marked window. A
depth-one window contains two vertices and a depth-two window contains
three, so at most

\[
2E_1+3E_2+3E_1=5E_1+3E_2=o(W)
\tag{4.2}
\]

vertices are deleted. The survivors form paths and possibly untouched
cycles. Cut each untouched cycle once. If \(d\) vertices were deleted, the
number of resulting path components is at most \(B+d=o(W)\). Every
duplicated colored window except its chosen representative was broken, so
all retained colors are conflict-free through depth two.

Conversely, suppose that \(\mathcal P\) has \(v=W-o(W)\) vertices and
\(p=o(W)\) components. It contains exactly \(v-p=W-o(W)\) depth-one
windows and at least \(v-2p=W-o(W)\) depth-two windows. Injectivity gives

\[
N_1-H_1\ge v-p,
\qquad
N_2-H_2\ge v-2p.
\]

Since \(W-N_1,W-N_2=o(W)\), both \(H_1\) and \(H_2\) are \(o(W)\).
\(\square\)

There is also a stronger exact tripartite packing target. Let
\(\mathfrak H_2\) have vertex parts

\[
\binom{[n]}m,
\qquad
\binom{[n]}{m-1},
\qquad
\binom{[n]}{m-2},
\]

and let a directed cyclic order contribute the union of its three complete
interval families at these ranks. A matching of \(p\) hyperedges is exactly
a \(p\)-wreath packing globally conflict-free through lower depth two;
upper conflicts are then absent by (2.4). The largest possible value is

\[
p\le\left\lfloor\frac{N_2}{n}\right\rfloor.
\]

If equality up to the remainder is attained and
\(s=N_2-pn<n\), then

\[
M_2=s,
\qquad
M_1=N_1-N_2+s,
\qquad
M_0=W-N_2+s.
\]

Substitution in Theorem 3.1 gives

\[
L_{[m-2,m+2]}-W
=4p+(W-N_2)+2(N_1-N_2)+4s
=\left(16+o(1)\right)\frac Wm.
\tag{4.3}
\]

The existence of this matching is unproved. For this relaxed near-factor
route, (4.3) proves that conversion is no longer the issue; the remaining
theorem is existence of the saturated tripartite matching among true
wreaths. This route is sufficient for the central-band OR conversion, but it
is not equivalent to (D2WF): extending the partial packing to a spanning
exact factor is a separate unproved requirement.

## 5. A deterministic true-wreath nonpropagation theorem

The next construction uses actual cyclic-order wreaths and preserves every
rankwise total and point-margin identity.

Fix \(h\ge1\), put

\[
d=2h+1,
\qquad
m=dt+h,
\qquad
n=2m+1=d(2t+1),
\qquad t\ge1.
\tag{5.1}
\]

Let \(b=2t+1\), and partition \([n]\) into ordered \(d\)-blocks

\[
B_j=\{b_{j,0},b_{j,1},\ldots,b_{j,d-1}\},
\qquad j\in\mathbb Z_b.
\]

Define two cyclic orders with the same cyclic block order by

\[
\pi=
(B_0^{(0)},B_1^{(0)},\ldots,B_{b-1}^{(0)}),
\qquad
B_j^{(0)}=(b_{j,0},b_{j,1},\ldots,b_{j,d-1}),
\tag{5.2}
\]

and

\[
\sigma=
(B_0^{(1)},B_1^{(1)},\ldots,B_{b-1}^{(1)}),
\qquad
B_j^{(1)}=(b_{j,1},\ldots,b_{j,d-1},b_{j,0}).
\tag{5.3}
\]

For a cyclic order \(\rho\), let \(\mathcal C_L(\rho)\) be the family of
all cyclic length-\(L\) interval sets.

### Lemma 5.1 (block-rotation interval lemma)

For every \(d\le L\le n-d\),

\[
\boxed{
\mathcal C_L(\pi)\cap\mathcal C_L(\sigma)
=
\begin{cases}
\varnothing,&d\nmid L,\\[2mm]
\{\text{unions of \(L/d\) consecutive whole blocks}\},&d\mid L.
\end{cases}}
\tag{5.4}
\]

In the second case the intersection has exactly \(b\) members.

#### Proof

First suppose that a common interval has proper block support. Its first
block intersection must be a suffix in both internal orders, and its last
block intersection must be a prefix in both internal orders. For
\(1\le a<d\), the size-\(a\) prefixes in the two orders are

\[
\{0,1,\ldots,a-1\},
\qquad
\{1,2,\ldots,a\},
\]

while their size-\(a\) suffixes are

\[
\{d-a,\ldots,d-1\},
\qquad
\{d-a+1,\ldots,d-1,0\}.
\]

Neither pair agrees. Hence both endpoint blocks must be whole, and the
interval is a union of consecutive whole blocks.

If a common interval meets every block, its complement is also a common
cyclic interval and has length at least \(d\). An interval boundary splits
at most two blocks, while \(b\ge3\), so the complement has proper block
support. The preceding argument applied to the complement again shows that
the original interval is a union of whole blocks.

Such an interval has length divisible by \(d\). Conversely, every union of
consecutive whole blocks is visibly an interval in both orders. There are
exactly \(b\) possible cyclic starts because \(1\le L/d\le b-1\).
\(\square\)

### Theorem 5.2 (true-wreath failure of local depth propagation)

The two cyclic orders (5.2)--(5.3) define vertex-disjoint genuine wreath
cycles. Their lower colors are mutually disjoint through depths
\(1,\ldots,h-1\), and their upper colors are mutually disjoint through
depths \(1,\ldots,h\). At lower depth \(h\), however, they share exactly

\[
\boxed{
b=\frac{n}{2h+1}}
\tag{5.5}
\]

colors. Thus the duplicate excess is a fraction

\[
\frac{b}{2n}=\frac1{2(2h+1)}
\tag{5.6}
\]

of the two cycles' depth-\(h\) occurrences.

#### Proof

The Johnson cycle obtained from a cyclic-order wreath has vertices
\(I_\rho(j,m)\). Its lower and upper depth-\(q\) colors are respectively

\[
I_\rho(j+q,m-q)
\qquad\text{and}\qquad
I_\rho(j,m+q).
\tag{5.7}
\]

For \(0\le q<h\),

\[
m-q=dt+h-q\not\equiv0\pmod d,
\]

whereas \(m-h=dt\). For \(1\le q\le h\),

\[
m+q=dt+h+q\not\equiv0\pmod d.
\]

All these lengths lie between \(d\) and \(n-d\). Lemma 5.1 therefore
proves every disjointness assertion and says that the common depth-\(h\)
family consists exactly of the \(b\) unions of \(t\) consecutive blocks.
The middle length \(m\) is not divisible by \(d\), so the two wreath cycles
are vertex-disjoint. \(\square\)

For depth two, take \(h=2\). Then

\[
m=5t+2,
\qquad
n=10t+5.
\]

The two actual wreath cycles are perfectly conflict-free between components
in both depth-one colors and in the upper depth-two colors, but share exactly
\(n/5\) lower depth-two colors. This is a \(1/10\) collision fraction among
their combined depth-two occurrences.

### Flat margins and robust edit distance

The common family in (5.5) is itself a \(1\)-design. It has \(b\) members,
and each point lies in exactly \(t\) of the cyclic unions of \(t\)
consecutive blocks.

More generally, every cyclic rank-\(r\) interval family has total mass \(n\)
and point degree exactly \(r\). Hence, for every \(r\), the signed profile

\[
\delta_r(A)
=\mathbf1_{\{A\in\mathcal C_r(\pi)\}}
-\mathbf1_{\{A\in\mathcal C_r(\sigma)\}}
\]

satisfies

\[
\sum_A\delta_r(A)=0,
\qquad
\sum_{A\ni x}\delta_r(A)=0
\quad(x\in[n]).
\tag{5.8}
\]

Thus the collision is compatible with exact zero total and point margins.

The \(b\) common depth-\(h\) windows on either cycle start \(d=2h+1\)
positions apart and each uses \(h\) consecutive old Johnson edges. They are
therefore pairwise edge-disjoint on each component. Consider any new path or
cycle packing on the same middle vertices, and measure its edit cost by the
number of old transitions it fails to retain. If all \(h\) edges of one old
window survive, its duplicate color survives. For each of the \(b\) common
colors, at least one of its two old windows must therefore be broken, while
one deleted old edge can break at most one such window. Consequently

\[
\boxed{
\text{at least }\frac n{2h+1}\text{ old transitions must be changed}.}
\tag{5.9}
\]

For \(h=2\), at least \(n/5\) transitions must change. The counterexample
therefore rules out not only automatic propagation but every sparse
old-transition-edit repair on these fixed middle supports. It does not rule
out a reconstruction that replaces middle vertices.

Its exact scope matters: this is a two-component partial packing. It is not
proved that the prescribed pair extends to one spanning exact factor, so it
does not refute the global implication \(H_1=o(W)\Rightarrow H_2=o(W)\)
inside exact factors.

## 6. A near-spanning cycle-packing counterexample

The preceding construction uses true wreaths but only two components. The
next theorem is near-spanning, at the price of using general Johnson cycles
rather than wreath cycles.

Put

\[
V=\binom{2m}{m},
\qquad
C=\binom{2m}{m-1}=\binom{2m}{m+1}.
\]

### Theorem 6.1 (near-spanning depth-one rainbowness with collapsed depth two)

There is a sequence of vertex-disjoint cycle families \(\mathcal Q_m\) in
\(J(2m,m)\) such that:

1. their cycles cover \(V-o(V)\) middle vertices;
2. all lower depth-one colors are globally distinct and cover
   \(C-o(V)\) rank-\((m-1)\) sets;
3. all upper depth-one colors are globally distinct and cover
   \(C-o(V)\) rank-\((m+1)\) sets;
4. the number of distinct lower depth-two colors is \(o(V)\).

Thus a near-spanning, globally two-sided-rainbow cycle packing can miss
\((1-o(1))V\) depth-two lower targets.

We use the proved fixed-uniformity near-perfect-matching theorem in the
following exact form: for fixed \(k\), if a \(k\)-uniform hypergraph has
maximum degree \(D\to\infty\), minimum degree \((1-o(1))D\), and maximum
pair-codegree \(o(D)\), then it has a matching leaving \(o(|V|)\) vertices
uncovered.

#### Proof

Fix first an integer \(\ell\ge5\). Choose a core

\[
S\in\binom{[2m]}{m-2}
\]

and an undirected cyclic order

\[
\gamma=(v_0,v_1,\ldots,v_{\ell-1})
\]

of \(\ell\) distinct points of \(S^c\). Define

\[
X_i=S\cup\{v_i,v_{i+1}\},
\qquad i\in\mathbb Z_\ell.
\tag{6.1}
\]

These vertices form a simple Johnson \(\ell\)-cycle. Its edge colors are

\[
X_i\cap X_{i+1}=S\cup\{v_{i+1}\},
\tag{6.2}
\]

and

\[
X_i\cup X_{i+1}=S\cup\{v_i,v_{i+1},v_{i+2}\}.
\tag{6.3}
\]

Both color families are internally injective. But every cyclic depth-two
lower color is

\[
X_i\cap X_{i+1}\cap X_{i+2}=S.
\tag{6.4}
\]

Create a \(3\ell\)-uniform hypergraph with tagged vertex parts

\[
\binom{[2m]}m,
\qquad
\binom{[2m]}{m-1},
\qquad
\binom{[2m]}{m+1},
\]

and let one hyperedge consist of the \(\ell\) objects in each of
(6.1)--(6.3). The hypergraph is simple: intersecting its middle objects
recovers \(S\), and subtracting \(S\) recovers the edge set of the undirected
cycle \(\gamma\).

If \(E\) is the number of gadgets, transitivity and incidence counting give
the exact degrees

\[
E=\binom{2m}{m-2}\binom{m+2}{\ell}\frac{(\ell-1)!}{2},
\]

\[
D_0=\frac{E\ell}{V},
\qquad
D_-=D_+=\frac{E\ell}{C}
=\frac{m+1}{m}D_0.
\tag{6.5}
\]

For fixed \(\ell\), these degrees tend to infinity with \(m\).

The maximum pair-codegree is \(o(D_-)\) for fixed \(\ell\). To see this,
fix one tagged object \(A\). Under its setwise stabilizer, the orbit of any
distinct co-occurring tagged object \(A'\) has size at least \(m-1\).
Indeed, a stabilizer orbit has size

\[
\binom{|A|}{|A\cap A'|}
\binom{2m-|A|}{|A'\setminus A|}.
\]

Orbit size one can only arise from equality or complementation. Equality is
excluded, and complementation is impossible because every two objects in
one gadget contain the nonempty core \(S\). A gadget through \(A\) contains
at most \(3\ell-1\) possible partners. Orbit double counting therefore
gives

\[
\frac{\Delta_2}{D_-}
\le\frac{3\ell-1}{m-1}.
\tag{6.6}
\]

For fixed \(\ell\), the uniformity is fixed, all degrees are
\((1+o(1))D_-\), and (6.6) is \(o(1)\). The fixed-uniformity
near-perfect-matching theorem therefore supplies a matching leaving
\(o_\ell(V)\) vertices uncovered in the union of all three tagged parts.

If the matching has \(p\) gadgets, its lower part gives

\[
\ell p=C-o_\ell(V).
\tag{6.7}
\]

Consequently it misses only

\[
V-\ell p=V-C+o_\ell(V)=o(V)
\]

middle vertices, and it has the two global depth-one rainbowness properties.
By (6.4), its lower depth-two support has size at most \(p\).

Finally diagonalize the fixed-\(\ell\) theorem: choose
\(\ell=\ell(m)\to\infty\) sufficiently slowly that the unmatched term is
still \(o(V)\) and \(\ell=o(m)\). Then (6.7) gives

\[
p=O(V/\ell)=o(V).
\]

Since

\[
\binom{2m}{m-2}=(1-o(1))V,
\]

the missing lower depth-two support is \((1-o(1))V\). \(\square\)

This theorem is a genuine near-spanning cycle-packing counterexample to
every black-box implication from two-sided depth-one rainbowness to depth
two. It is not an exact-factor counterexample: the cycles in (6.1) repeat
one depth-two core internally, whereas a true wreath cycle has \(n\)
distinct cyclic intervals at every nontrivial rank. The fixed point margins
of an exact factor are also absent. Theorem 5.2 supplies the complementary
true-wreath and zero-margin obstruction.

## 7. The Greene--Kleitman forest needs linear replacement

The proved two-sided-rainbow forest can be projected off the middle rank.
For \(r<N/2\), apply the Greene--Kleitman symmetric-chain construction to
every \((r-1)\)-set. Its chain contains

\[
S\subset T\subset U,
\qquad
|S|=r-1, |T|=r, |U|=r+1.
\]

Join \(T\) to the other rank-\(r\) set between \(S\) and \(U\). The
resulting graph on rank \(r\) is a spanning forest; every lower color occurs
once and all selected upper colors are distinct.

The obstruction is its branching.

### Proposition 7.1 (exact off-central indegree law)

Let \(A_{N,r,j}\) be the number of rank-\(r\) vertices having indegree
exactly \(j\) in the oriented Greene--Kleitman forest. Then

\[
\boxed{
A_{N,r,j}=\binom{N-j-1}{r-j}}
\qquad(0\le j\le r),
\tag{7.1}
\]

and consequently

\[
\boxed{
|\{X:\deg^-(X)\ge t\}|
=\binom{N-t}{r-t}.}
\tag{7.2}
\]

#### Proof

Use the Greene--Kleitman parenthesis matching, with \(0\) opening and
\(1\) closing, and put \(h=N-2r>0\). A rank-\(r\) word with \(a\)
unmatched ones has \(a+h\) unmatched zeros and a factorization into
\(2a+h+1\) Dyck factors. The incoming forest edges correspond exactly to
the primitive components of the central Dyck factor.

Let \(C(x)\) be the Catalan generating function. A Dyck word having exactly
\(j\) primitive components contributes \((xC(x))^j\). Summing over \(a\)
gives

\[
A_{N,r,j}
=\sum_{a=0}^{r-j}
[x^{r-a-j}]C(x)^{2a+h+j}.
\tag{7.3}
\]

Set \(k=r-a-j\). Since \(2r+h=N\), (7.3) becomes

\[
A_{N,r,j}
=\sum_{k=0}^{r-j}
[x^k]C(x)^{N-j-2k}.
\]

Lagrange inversion gives

\[
[x^k]C(x)^b
=\frac{b}{2k+b}\binom{2k+b}{k}.
\]

Here \(2k+b=N-j\), and the summand is

\[
\binom{N-j-1}{k}
-\binom{N-j-1}{k-1}.
\]

The sum telescopes to (7.1). Summing (7.1) over \(j\ge t\) and applying the
hockey-stick identity proves (7.2). \(\square\)

Now take

\[
N=2m+1,
\qquad
r=m-1.
\]

The forest has \(N_1\) vertices and \(N_2\) edges. Its lower edge colors
are every rank-\((m-2)\) target once, and its upper colors are \(N_2\)
distinct middle sets. Thus it is exactly the tempting two-sided-rainbow
depth-two skeleton for the rank-\((m-1)\) occurrence graph.

The number of indegree-at-least-two labels is

\[
A_m=\binom{2m-1}{m-3}.
\tag{7.4}
\]

The number of outdegree-zero roots is

\[
R_m=N_1-N_2,
\]

so at least \(A_m-R_m\) labels have total forest degree at least three.

An exact wreath factor's rank-\((m-1)\) occurrence graph has \(W\)
occurrence vertices and maximum degree two. Its number of copies beyond one
per possible label is only

\[
S_m=W-N_1.
\]

Suppose \(\eta\) rank-\((m-1)\) labels are omitted, and all but \(d\) forest
edges are embedded label-preservingly into any maximum-degree-two graph on
the \(W\) occurrence vertices. A nonroot branching label must be omitted,
split over at least two occurrence copies, or incident to a deleted edge.
There are \(S_m+\eta\) extra copies after accounting for the omitted labels,
and one deleted edge has at most two branching endpoints. Therefore

\[
A_m-R_m
\le
\eta+(S_m+\eta)+2d,
\]

and hence

\[
\boxed{
d\ge
\left\lceil
\frac{A_m-R_m-S_m-2\eta}{2}
\right\rceil_+.}
\tag{7.5}
\]

Here \(\lceil x\rceil_+=\max\{0,\lceil x\rceil\}\).

The exact normalized quantities are

\[
\frac{A_m}{W}
=\frac{(m-1)(m-2)}{2(m+2)(2m+1)},
\]

\[
\frac{R_m}{W}
=\frac{4m}{(m+2)(m+3)},
\qquad
\frac{S_m}{W}=\frac2{m+2}.
\tag{7.6}
\]

Thus, whenever \(\eta=o(W)\),

\[
\boxed{d\ge(1/8-o(1))W.}
\tag{7.7}
\]

This obstruction already holds for arbitrary degree-two occurrence graphs.
Requiring \(n\)-cycle components, exact upper labels, and wreath single-run
geometry can only impose further restrictions. Therefore the particular
Greene--Kleitman forest cannot be turned into the desired depth-two
occurrence graph by \(o(W)\) color-preserving edits. A different
born-linear, wreath-extendible rainbow construction is not ruled out.

## 8. Final theorem and scope audit

### Proved inputs

The report uses only three prior existence tools: exact middle wreath
factors, the Greene--Kleitman two-sided-rainbow forest, and the
fixed-uniformity near-perfect-matching theorem stated in Section 6. All
duality, conversion, obstruction, degree, codegree, and edit estimates used
here are proved in the report. No unproved lemma is invoked as if it were a
theorem.

### Proved here

1. For every exact wreath factor, upper depth two is exactly dual, with
   multiplicity, to lower depth one; only lower depth two is new.
2. The intact-cycle construction (3.2)--(3.3) is a deterministic literal
   conversion, with all constants and seam costs explicit.
3. Joint depth-one/depth-two support is equivalent to one near-spanning
   conflict-free path subfactor inside the same exact factor.
4. The block-rotation pair is a deterministic actual-wreath obstruction at
   every fixed depth, with flat point margins and an exact lower bound for
   hitting all displayed old duplicate windows. No completed packing
   attaining that bound is asserted.
5. The core-star matching theorem gives a near-spanning two-sided-rainbow
   Johnson cycle packing with asymptotically vanishing depth-two support.
6. The off-central Greene--Kleitman forest needs
   \((1/8-o(1))W\) edge replacements before it can enter any exact-factor
   occurrence graph with only \(o(W)\) omitted labels.

### Not proved

1. The two true wreaths in Theorem 5.2 are not proved extendible to one
   spanning exact factor.
2. The near-spanning cycles in Theorem 6.1 are not wreath cycles and do not
   have exact factor point margins.
3. The tripartite wreath matching after (4.3) and the exact-factor statement
   (D2WF) both remain open. They are distinct because extendibility of the
   partial matching to an exact factor is unproved.
4. A fixed depth-two band does not make the outer-tail cost \(o(W)\); hence
   this report does not prove the coefficient-one contiguous-OR theorem.
5. No labelled common-owner synchronization statement follows from these
   unlabelled support theorems.

The exact depth-one-to-depth-two conclusion is therefore neither a blanket
success nor a blanket failure. Success propagates automatically to the
upper depth-two colors and literal conversion is complete. It fails for the
new lower colors under local, componentwise, generic near-spanning-cycle,
and Greene--Kleitman black-box hypotheses. What remains is precisely a new
global integral theorem inside one exact wreath factor: (D2WF).
