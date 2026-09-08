# Dimension-uniform Pascal Shadow--Braid induction interface

Date: 2026-07-31  
Status: exact conditional theorem and parity audit; no all-\(k\) construction
is claimed  
Scope: Pascal owner lifts, component-neutral Catalan port factors, protected
block braids, variable P/Q schedules, pins, and maximal-common-cap compilers

## 0. Verdict

The K16 endpoint-reroot/common-cap certificate and the K15-to-K17
four-sector Pascal diamond fit one exact induction interface, but they close
different branches of it.

* The K16 construction closes one finite odd-to-even branch: exact two-shore
  ownership, an upper-safe protected endpoint reroot, a variable staircase
  with a legal singleton pin, and one global common-cap compiler.
* The K15-to-K17 construction closes the middle-ownership and immediate
  lower-shadow part of an odd-to-odd Pascal diamond.  Its frozen child is a
  17-cycle factor with a complete immediate lower palette, but it has 1,739
  immediate upper holes, 4,045 total upper holes, and a catastrophic
  residence frontier.  Every direct-formula factor also has a 60-target
  opposite-occurrence obstruction.

Thus K16 proves that the compiler branch can close once a good braid is
found; the K17 factor proves that a Catalan-leave owner deck can be built
integrally.  Neither fact supplies the other's missing hypothesis.

The component-neutral law in Theorems 2.2--2.4 sharpens the odd branch.
The direct four-sector formulas force the exact
\(AA/XX/XA/YY/AY\) edge counts and stub budget, but their separated
cap-two choice traps the \(AA\) sector in sealed cycles.  The nonvacuous
residual object is a coupled cap-two/socket path factor with exactly
\(C_r\) free \(X\)-stubs and \(C_r\) free \(Y\)-stubs.  Once that factor is
endpoint-balanced, any compatible \(c\)-path cover of the \(U\)-deck can be
inserted into the Catalan macro gaps without changing the untagged lower-q1
capacity.  Thus a standalone \(U\) Hamilton path is not the recursive
invariant.  The exact replacement is the coupled residual path factor plus a
cyclic occurrence-labelled port/direct-seam injection and one distinguished
opening.

The exact dimension-uniform Shadow--Braid lemma is proved in Section 4.  A
useful all-\(k\) induction can run along the odd spine:

\[
 2r-1\longrightarrow
 \begin{cases}
 2r&\text{by an odd-to-even facet braid},\\
 2r+1&\text{by an odd-to-odd four-sector diamond}.
 \end{cases}
\]

This bypasses the fixed K16-to-K17 even-to-odd occurrence-selection no-go.
It still needs a **regenerative odd factor** at \(2r+1\), not merely a
universal word there.  Producing that factor with residence, full upper
support, and compiler-compatible protected ports is the unresolved theorem.

## 1. Exact parity and Catalan arithmetic

Let \(r\ge2\), and let the odd parent have ground set \(\Omega\),

\[
 |\Omega|=2r-1,qquad
 M={2r-1\choose r}={2r-1\choose r-1},
\]

and put

\[
 C_r=\operatorname{Cat}_r=\frac1{r+1}{2r\choose r}
     =\frac{2M}{r+1}.
\tag{1.1}
\]

### 1.1 Odd to even

After adjoining \(x\), the even middle layer is

\[
 {\Omega\cup\{x\}\choose r}
 = {\Omega\choose r}
   \mathbin{\dot\cup}
   \bigl(x+{\Omega\choose r-1}\bigr).
\tag{1.2}
\]

Both shores have size \(M\), and the child width is \(2M\).

### 1.2 Even to odd

For an even ground set \(\Xi\) of size \(2r\), adjoining \(y\) gives

\[
 {\Xi\cup\{y\}\choose r+1}
 = {\Xi\choose r+1}
   \mathbin{\dot\cup}
   \bigl(y+{\Xi\choose r}\bigr).
\tag{1.3}
\]

The two shore sizes are

\[
 {2r\choose r+1}=2M-C_r,qquad {2r\choose r}=2M.
\tag{1.4}
\]

The Catalan mismatch in (1.4) is structural.  An even-to-odd construction
needs one occurrence of every old rank-\((r+1)\) owner, not merely the
marked copy of the even middle deck.

### 1.3 The odd-to-odd Pascal diamond

Expanding both shores of (1.3) through the first new coordinate \(x\) gives

\[
 {\Omega\cup\{x,y\}\choose r+1}
 =U\mathbin{\dot\cup}X\mathbin{\dot\cup}Y
  \mathbin{\dot\cup}A,
\tag{1.5}
\]

where

\[
 \begin{array}{c|c|c}
 \text{sector}&\text{old rank}&\text{size}\\ \hline
 U& r+1&M-C_r\\
 X& r&M\\
 Y& r&M\\
 A& r-1&M.
 \end{array}
\tag{1.6}
\]

Indeed the unmarked even-to-odd shore is \(U\dot\cup X\), of size
\(2M-C_r\), and the marked shore is \(Y\dot\cup A\), of size \(2M\).
This is the exact four-sector Pascal diamond.

For the monotone-deadline excess \(d_k\), the proved parity recurrences give

\[
 d_{2r}\in\{d_{2r-1}-1,d_{2r-1}\},
 \qquad
 d_{2r+1}\in\{d_{2r},d_{2r}+1\}.
\tag{1.7}
\]

Thus a facet branch may need the same depth or one less, while a union branch
may need the same depth or one more.  For K15, K16, and K17 all three depths
are three; this is a parity plateau, not a favourable buffer drop.

## 2. The dimension-uniform four-sector factor lemma

Assume in this section that \(r\ge3\).  Let \(F\) be a directed Johnson
2-factor on the rank-\(r\) layer of
\(\Omega\).  Index its vertices by \(i\), write \(T_i\) for vertex \(i\),
and let \(\operatorname{succ}(i)\) and \(\operatorname{pred}(i)\) be the
successor and predecessor inside the same directed component.  Put

\[
 C_i=T_i\cap T_{\operatorname{succ}(i)},qquad
 V_i=T_i\cup T_{\operatorname{succ}(i)}.
\tag{2.1}
\]

Call \(F\) **diamond-ready at the owner level** when:

1. the \(C_i\) enumerate \({\Omega\choose r-1}\) exactly once;
2. every member of \({\Omega\choose r+1}\) occurs among the \(V_i\), and
   an occurrence transversal \(I\) selects one occurrence of each; and
3. in the bipartite graph

   \[
    Z\sim i\quad\Longleftrightarrow\quad
    Z\in{\Omega\choose r-2},\ i\in I,\ Z\subset C_i,
   \tag{2.2}
   \]

   there is a simple spanning factor of degree two on both shores.

The two shores in (2.2) have size \(M-C_r\).  The unselected Catalan leave

\[
 J=\operatorname{Idx}(F)\setminus I
\]

has forced size

\[
 |J|=M-(M-C_r)=C_r.
\tag{2.3}
\]

### Theorem 2.1 (Pascal diamond factor)

Every owner-level diamond-ready factor produces a spanning simple Johnson
2-factor on the rank-\((r+1)\) layer of
\(\Omega\cup\{x,y\}\).  Its edge intersections enumerate the complete
rank-\(r\) layer exactly once.

#### Proof

For every parent edge index define the owners

\[
 A_i=C_i\cup\{x,y\},\quad
 X_i=T_i\cup\{x\},\quad
 Y_i=T_i\cup\{y\},
\]

and for \(i\in I\) define \(U_i=V_i\).  The four owner classes are exactly
the four disjoint sectors in (1.6).

Write \(K\) for the degree-two factor in (2.2).  If the two \(K\)-neighbours
of \(Z\) are \(i,j\), include

\[
 A_iA_j.
\tag{2.4}
\]

For every parent index \(i\), include

\[
 \begin{cases}
 X_iX_{\operatorname{succ}(i)},&i\in I,\\
 X_iA_i,&i\in J,
 \end{cases}
 \qquad
 \begin{cases}
 Y_iY_{\operatorname{succ}(i)},&i\in I,\\
 A_iY_{\operatorname{succ}(i)},&i\in J.
 \end{cases}
\tag{2.5}
\]

Finally put

\[
 L_i=\begin{cases}
 U_{\operatorname{pred}(i)},&\operatorname{pred}(i)\in I,\\
 X_i,&\operatorname{pred}(i)\in J,
 \end{cases}
 \qquad
 R_i=\begin{cases}
 U_i,&i\in I,\\
 Y_i,&i\in J,
 \end{cases}
\tag{2.6}
\]

and include \(L_iR_i\).  The intersections of (2.4)--(2.6) are,
respectively,

\[
 Z+xy,qquad C+x,qquad C+y,qquad T.
\tag{2.7}
\]

Indeed, if \(Z\) has neighbours \(i,j\), then the distinct rank-\((r-1)\)
sets \(C_i,C_j\) both contain \(Z\), so
\(A_i\cap A_j=Z+xy\).  The two cases of each edge in (2.5) have
intersections \(C_i+x\) and \(C_i+y\).  All four cases in (2.6) have
intersection \(T_i\); in the only nonliteral case,
\(U_{\operatorname{pred}(i)}\cap U_i=T_i\), because a transversal cannot
select two occurrences of the same union owner.

These four classes partition the child rank-\(r\) layer and every member
occurs once.  The degree ledger is also literal: selected \(A_i\)'s receive
their two \(K\)-edges, leave \(A_i\)'s receive their \(X\)- and \(Y\)-turn
edges, and every \(X_i,Y_i,U_i\) receives exactly two edges from
(2.5)--(2.6).  Simplicity of \(K\) excludes loops; two different \(Z\)'s
cannot induce the same \(A_iA_j\), because two distinct common
rank-\((r-2)\) subsets would force \(C_i=C_j\).  This is exactly the
dimension-free proof of the K15-to-K17 factor theorem.
\(\square\)

Theorem 2.1 proves middle ownership and an immediate-lower rainbow.  It does
not prove that the child factor's adjacent unions cover the complete
rank-\((r+2)\) layer, that its components can be braided safely, that it is
resident, or that it has a common-cap compiler.

### Theorem 2.2 (component-neutral untagged lower-q1 identity)

Put

\[
 b=C_r,\qquad N=M-b={2r-1\choose r+1}.
\tag{2.8}
\]

Partition each of the \(A,X,Y\) owner decks into \(b\) nonempty directed
Johnson paths and group one path from each deck into each of \(b\) legal
common-orientation macros.  In the reverse orientation a macro is

\[
 \overleftarrow X_i\,\overleftarrow A_i\,\overleftarrow Y_i,
\tag{2.9}
\]

so the \(b-1\) internal macro gaps have a \(Y\)-endpoint on the left and an
\(X\)-endpoint on the right.  Partition the complete \(N\)-vertex \(U\)-deck
into \(c\) nonempty directed Johnson paths, where

\[
 1\le c\le\min(N,b-1).
\tag{2.10}
\]

Assign the \(c\) paths injectively to \(c\) macro gaps.  At an assigned gap
join the two macro endpoints through the oriented \(U\)-path by two legal
ports; at every unassigned gap use one legal direct \(Y\)-to-\(X\) seam.
Then the child lower-q1 edge-slot ledger is

\[
 \begin{array}{c|c}
 \text{new-coordinate signature}&\text{number of slots}\\ \hline
 xy&M-b=N\\
 x&(M-b)+b=M\\
 y&(M-b)+b=M\\
 00&(N-c)+2c+(b-1-c)=M-1.
 \end{array}
\tag{2.11}
\]

In particular, the untagged slot count is independent of the number of
\(U\)-components.  Standalone Hamiltonicity of the \(U\)-deck is therefore
neither a counting nor a connectivity requirement for this braid topology.

If, in addition, all edge-intersection colours in each row of (2.11) are
injective, then the \(xy,x,y\) palettes are complete and the untagged palette
is

\[
 {\Omega\choose r}\setminus\{H\}
\tag{2.12}
\]

for one uniquely determined colour \(H\).  Conversely, these injectivity
conditions are necessary for a one-hole lower-q1-rainbow braid of this form.

#### Proof

A path cover of \(n\) vertices by \(t\) nonempty paths has \(n-t\) internal
edges.  Hence the internal \(A,X,Y\) path counts are all \(M-b=N\).  The
\(b\) internal \(X\)-to-\(A\) sockets add \(b\) one-\(x\) slots, and the
\(b\) internal \(A\)-to-\(Y\) sockets add \(b\) one-\(y\) slots.  This gives
the first three rows of (2.11).

The \(U\)-path cover has \(N-c\) internal untagged edges.  Its \(c\) inserted
paths contribute \(2c\) untagged ports, while the unassigned macro gaps
contribute \(b-1-c\) untagged direct seams.  Therefore

\[
 (N-c)+2c+(b-1-c)=N+b-1=M-1,
\tag{2.13}
\]

which proves component neutrality.  The four signature palettes have sizes

\[
 \left|{\Omega\choose r-2}\right|=N,qquad
 \left|{\Omega\choose r-1}\right|=M,qquad
 \left|{\Omega\choose r-1}\right|=M,qquad
 \left|{\Omega\choose r}\right|=M.
\tag{2.14}
\]

Thus injectivity and (2.11) fill the first three palettes and all but one
member of the fourth.  Different signatures are automatically disjoint.
\(\square\)

The word “insertion” in Theorem 2.2 is topological, not the subdivision of a
fixed labelled Johnson seam.  If the old projections of a chosen gap are
\(L\) on the \(Y\)-side and \(R\) on the \(X\)-side, a direct seam is legal
exactly when \(L=R\), and its colour is that common set.  An inserted path
\((V_1,\ldots,V_s)\) instead requires

\[
 L\subset V_1,\qquad R\subset V_s,
\tag{2.15}
\]

and its port colours are \(L,R\).  Lower-rainbow injectivity therefore forces
\(L\ne R\) at an inserted gap.  The macro order and endpoint labels must be
chosen jointly; one cannot first freeze a legal direct seam and subdivide it.
A simple Johnson path also need not be lower-rainbow: for a rank-\(r\) set
\(T\) and distinct outside elements \(a,b,c\), the path
\((T+a,T+b,T+c)\) repeats intersection colour \(T\).  Consequently (2.11)
is unconditional for slots, while (2.12) needs the stated global
injectivity gate.

If the \(U\)-internal bank is already rainbow, it occupies \(N-c\) colours,
so its residual untagged palette has size

\[
 M-(N-c)=b+c.
\]

The occurrence-labelled external demand has size

\[
 2c+(b-1-c)=b+c-1.
\tag{2.16}
\]

Thus the exact remaining lower-q1 problem is a near-perfect injection of the
port and direct-seam slots into this residual palette, leaving one colour.
This is the component-neutral matching/CSP interface; it contains no demand
that the \(U\)-paths first be joined to one standalone path.

There is an equivalent cyclic ledger.  With \(b\) cyclic macro gaps and
\(c\le b\) inserted \(U\)-paths, the untagged count is

\[
 (N-c)+2c+(b-c)=M.
\tag{2.17}
\]

If this cyclic palette is injective, opening one retained direct gap of
colour \(H\) gives the linear theorem and identifies the global boundary
hole.  Without a certified cyclic completion, (2.12) determines \(H\) only
as the unique complement; counts alone do not identify it with an endpoint.

Finally, pure-old upper targets are component-sensitive even though the
lower slot ledger is not.  In the interspersed braid an interval has neither
new tag only when it lies wholly inside one \(U\)-path.  Hence pure-old upper
coverage is equivalent to the protected condition

\[
 \forall Q\subseteq\Omega,\ |Q|\ge r+2,\quad
 \exists h,\ 1\le a\le q\le\ell_h:\quad
 Q=\bigcup_{t=a}^{q}V_{h,t}.
\tag{2.18}
\]

This is precisely the internal-witness side of the cut-support ledger in
Section 6.  Tagged upper targets, residence and collars, the P/Q schedule,
pins, and the global common cap remain SB1--SB4 obligations.  Thus Theorem
2.2 removes standalone \(U\)-Hamiltonicity from the regenerative topology;
it does not prove CSB\(_r\).

### Theorem 2.3 (forced balanced residual-sector ledger)

Return to an owner-level diamond-ready factor \((F,I,K)\) from Theorem 2.1.
Let \(R_0\) be the graph on the \(A,X,Y\) owners containing the
\(A_iA_j\) edges from (2.4) and all edges in (2.5), but none of the
untagged \(L_iR_i\) edges in (2.6).  Then

\[
 \begin{array}{c|ccccc}
 \text{edge family}&AA&XX&XA&YY&AY\\ \hline
 \text{count}&N&N&b&N&b.
 \end{array}
\tag{2.19}
\]

The \(AA\) edges enumerate every \(xy\)-tagged lower colour once, while
\(XX\cup XA\) and \(YY\cup AY\) enumerate every one-\(x\) and one-\(y\)
lower colour once.  Every \(A\)-owner has degree two in \(R_0\).  The only
degree-one owners are

\[
 \{X_{\operatorname{succ}(j)}:j\in J\},\qquad
 \{Y_j:j\in J\},
\tag{2.20}
\]

each a \(b\)-element set; all other \(X,Y\) owners have degree two.

#### Proof

The cap-two factor has one edge for each old rank-\((r-2)\) set, hence
\(N\) \(AA\)-edges.  For every \(i\in I\), (2.5) contributes one \(XX\)
and one \(YY\) edge, giving \(N\) of each.  For every \(i\in J\), it
contributes one \(XA\) and one \(AY\) edge, giving \(b\) of each.
Their intersections are respectively

\[
 Z+xy,\qquad C_i+x,\qquad C_i+y.
\]

The exact cap and facet decks prove the palette assertions.

If \(i\in I\), \(A_i\) has its two cap-factor edges; if \(i\in J\), it
has its \(XA\) and \(AY\) sockets.  Thus every \(A_i\) has degree two.
Every \(X_i\) has its index-\(i\) edge and has a predecessor edge exactly
when \(\operatorname{pred}(i)\in I\), yielding the first set in (2.20).
Every \(Y_i\) has its predecessor edge and has an index-\(i\) edge exactly
when \(i\in I\), yielding the second.  \(\square\)

The literal \(R_0\) can never itself be endpoint-balanced.  On the selected
indices \(I\), the \(AA\) graph is the projection of the degree-two factor
\(K\), hence is a nonempty union of sealed cycles, with no edge to an
\(A_j\), \(j\in J\).  Outside those unavoidable \(AA\) cycles, every open
component is automatically \(X\)-to-\(Y\): a parent component hit by \(t>0\)
leave indices produces exactly \(t\) such paths.  A parent component with no
leave index additionally produces one sealed \(X\)-cycle and one sealed
\(Y\)-cycle.  Thus (2.19) is the correct marginal ledger, but the separate
cap-two and outer factors must be coupled before it can be a macro path
cover.

The exact nonvacuous replacement is as follows.  Choose one \(AA\)-edge
\(e_Z=A_iA_j\) of colour \(Z+xy\) for every
\(Z\in{\Omega\choose r-2}\), allowing all compatible \(A\)-indices and
requiring \(\deg_{AA}(i)\le2\).  For every parent index \(i\), choose
\(\alpha_i,\beta_i\in\{0,1\}\) and use

\[
 \begin{array}{c|cc}
 &0&1\\ \hline
 \alpha_i&X_iX_{\operatorname{succ}(i)}&X_iA_i\\
 \beta_i&Y_iY_{\operatorname{succ}(i)}&A_iY_{\operatorname{succ}(i)}.
 \end{array}
\tag{2.21}
\]

Impose the coupled socket equation

\[
 \deg_{AA}(i)+\alpha_i+\beta_i=2
 \qquad(i\in\operatorname{Idx}(F)).
\tag{2.22}
\]

Call the resulting graph \(\widetilde R\).  Equations (2.21)--(2.22)
preserve all \(xy,x,y\) lower palettes exactly, and

\[
 \deg_{\widetilde R}(X_i)=2-\alpha_{\operatorname{pred}(i)},
 \qquad
 \deg_{\widetilde R}(Y_i)=2-\beta_i.
\tag{2.23}
\]

Thus its endpoint banks are

\[
 \{X_{\operatorname{succ}(i)}:\alpha_i=1\},
 \qquad
 \{Y_i:\beta_i=1\}.
\tag{2.24}
\]

Call \(\widetilde R\) a **balanced residual path factor** when it is acyclic
and every component pairs one endpoint from each bank in (2.24).  Since it
has \(3M\) vertices and

\[
 N+M+M=3M-b
\]

edges, it is then a spanning path cover by exactly \(b\) \(X\)-to-\(Y\)
macros.  Summing (2.22) and using endpoint balance forces
\(|\alpha|=|\beta|=b\), so its edge-family counts are again exactly
\((N,N,b,N,b)\).  This coupled factor, not the sealed literal \(R_0\), is
the residual object required for recursion.

### Theorem 2.4 (endpoint-compatible component-neutral closure)

Assume a balanced residual path factor \(\widetilde R\) exists.  Orient its
\(b\) macro paths from their \(X\)-endpoint to their \(Y\)-endpoint.  Let
the \(U\)-deck have a rainbow directed \(c\)-path cover,
\(1\le c\le\min(N,b-1)\).  Suppose there is a
cyclic order of the macros, an injection of the \(U\)-paths into \(c\) of
the \(b\) cyclic gaps, and a distinguished unassigned gap \(g_*\), such
that:

1. at every assigned gap the two endpoint containments in (2.15) hold;
2. at every unassigned gap the two old endpoint projections are equal, so
   the direct \(Y\)-to-\(X\) seam is Johnson;
3. the \(U\)-internal, port, and direct-seam intersection colours are
   jointly injective.

Then the resulting cyclic owner braid is a spanning Johnson cycle on the
complete child middle deck, and every child lower-q1 colour occurs exactly
once.  Deleting the direct seam at \(g_*\) gives a spanning Johnson path
whose sole missing lower-q1 colour is the colour \(H\) of that seam.

#### Proof

Endpoint balance partitions every \(A,X,Y\) owner into \(b\) macro paths.
The gap assignment joins those paths cyclically and inserts every \(U\)
owner exactly once, so the result is a spanning cycle.  Theorem 2.3 already
supplies the complete \(xy,x,y\) palettes.  Equation (2.17) and clause 3
supply all \(M\) untagged colours exactly once.  Opening \(g_*\) deletes
exactly its one untagged colour and no owner.  \(\square\)

The three clauses above are the exact **endpoint compatibility hypothesis**
at the owner/lower-q1 level.  They replace standalone \(U\)-Hamiltonicity by
a balanced residual macro factor, a compatible \(U\)-path cover, and one
occurrence-labelled palette injection.  For a recursive Shadow--Braid step
one must additionally require (2.18) for pure-old upper targets, literal
tagged-upper SB2, post-placement SB1, a protected pin for \(H\) and the
remaining SB3--SB4 compiler, optimum physical length, and a diamond-ready
auxiliary child factor with the next event/port record.  Under those added
hypotheses Theorem 4.1 makes the opened braid the next optimum-length
regenerative package.  Endpoint compatibility alone proves neither upper
coverage nor CSB\(_r\).

## 3. Exact residence, upper, and compiler data

Fix a proposed child middle chronology

\[
 T=(T_0,\ldots,T_{W-1}),qquad |T_i|=m,
\]

obtained by orienting and concatenating Pascal sector blocks.  Let a physical
P/Q schedule assign owner intervals

\[
 I_i=[s_i,q_i]\subseteq[0,L-1]
\]

with strictly increasing starts and deadlines.

### SB0: exact owner braid

The labelled sector rows are disjoint and their concatenation is a bijection
onto \({[k]\choose m}\).  Every declared seam used as a Johnson edge is
checked literally.  Johnson legality is useful for the shadow braid, but
owner exactness itself is the bijection statement.

### SB1: exact residence and chain alignment

The schedule is legal and chain-aligned:

\[
 s_i\le q_i,qquad s_{i+1}\le q_i+1.
\tag{3.1}
\]

For every coordinate and every interior maximal coordinate run \([a,b]\)
of \(T\), the exact safe-corridor inequality holds:

\[
 q_{a-1}+1<s_{b+1}.
\tag{3.2}
\]

Boundary runs are automatic.  In addition, every maximal-envelope letter

\[
 E_p=\bigcap_{i:p\in I_i}T_i
\tag{3.3}
\]

is nonempty, with the empty intersection defined as \([k]\) when no owner
interval contains \(p\).  Conditions (3.2)--(3.3) are exactly the uncapped
middle-row realization test.

For omission sets \(X,Y\), the full lower-cell atlas has exact scalar
surplus

\[
 \Omega_k=\sigma_k-\ell(X,Y),
\tag{3.4}
\]

where \(\ell\) is the arbitrary-P/Q loss.  The inequality
\(\Omega_k\ge0\) is necessary but is not a residence or compiler theorem.

### SB2: exact upper shadow

For every upper target \(U\subseteq[k]\), \(|U|>m\), an explicit row
interval is retained:

\[
 U=\bigcup_{i=a_U}^{b_U}T_i.
\tag{3.5}
\]

Adjacent-union or q1 completeness alone is not SB2.  All widths are required.

### SB3: simultaneous positional pins

Put

\[
 {\cal L}_m=\{S\subseteq[k]:1\le |S|<m\}.
\]

Let \(\Pi\) be an injective partial map from a subset of \({\cal L}_m\) to
distinct cells of the complete atlas.  Form the pinned envelope

\[
 E_p^{\Pi}=E_p\cap
 \bigcap_{(S,J)\in\Pi:\ p\in J}S.
\tag{3.6}
\]

It is nonempty, realizes every middle row, and realizes every protected pin.
Residual target--cell domains are rebuilt from \(E^{\Pi}\).  A multi-cell
pin remains a protected positive equation; only a one-cell singleton follows
from nonemptiness alone.

### SB4: one residual common cap

There is an injective assignment \(R\) of every unpinned member of
\({\cal L}_m\) to a distinct unpinned atlas cell such that

\[
 A_p=E_p^{\Pi}\cap
 \bigcap_{(S,J)\in R:\ p\in J}S
\tag{3.7}
\]

is nonempty at every position and reproduces every middle row and every
lower equality in \(\Pi\cup R\).

Separate sector matchings, ordinary Hall, or an assignment chosen before
pinning do not imply SB4.

## 4. The Shadow--Braid compiler lemma

### Theorem 4.1 (dimension-uniform Shadow--Braid lemma)

If a Pascal sector braid satisfies SB0--SB4, then the word

\[
 A=(A_0,\ldots,A_{L-1})
\]

from (3.7) is universal for contiguous union on \([k]\).  If
\(L=B(k)\), then \(\nu(k)=B(k)\).

#### Proof

SB3--SB4 realize every lower target and every middle owner literally.  For an
upper target, SB2 supplies a consecutive owner block \([a_U,b_U]\).
Chain alignment in SB1 makes

\[
 \bigcup_{i=a_U}^{b_U}I_i
\]

one physical interval.  Every letter in it is contained in some owner from
the block, while SB4 realizes every complete owner interval, so its union is
exactly \(U\).  The lower, middle, and upper rank ranges partition all
nonempty targets.  The independent monotone-deadline lower bound gives the
last assertion.  \(\square\)

The theorem is noncircular as a certificate interface.  It becomes circular
if SB2 or SB4 is renamed “the braid property” and then assumed without a
construction or independent certificate.

## 5. Exact parity transport and its limits

For a strict Johnson chronology put

\[
 (\partial T)_i=T_i\cap T_{i+1},\qquad
 (\nabla T)_i=T_i\cup T_{i+1}.
\tag{5.1}
\]

On a coordinate one-run/zero-gap pair \((\lambda,g)\), the local transforms
are

\[
 \partial:(\lambda,g)\mapsto(\lambda-1,g+1),
 \qquad
 \nabla:(\lambda,g)\mapsto(\lambda+1,g-1).
\tag{5.2}
\]

The \(\partial\) formula is pairwise valid when \(\lambda\ge2\), and the
\(\nabla\) formula is pairwise valid when \(g\ge2\).  A singleton one-run
vanishes under \(\partial\), while a singleton zero-gap vanishes under
\(\nabla\), merging its two neighbouring runs.  Accordingly the
fixed-depth facet/union identities below are bulk identities under these
exclusions and away from turn collars; all exceptions must be audited
literally.

### 5.1 Odd-to-even facet branch

The two bulk sectors are

\[
 T,qquad x+\partial T.
\tag{5.3}
\]

At child compiler depth \(d\), away from excluded singleton runs and the
seam collars, their bulk envelopes use parent packages

\[
 P_d(T)_i,qquad x+P_{d+1}(T)_{i+1}.
\tag{5.4}
\]

Thus the copied shore needs depth \(d\), while the facet shore needs one
additional parent run unit, unless an explicitly corrected shore and collar
replaces the strict facet chart.  On a depth-drop step this extra unit is
available from ordinary parent residence; on a plateau step it is an extra
hypothesis.  K15-to-K16 is a plateau and was closed by its authenticated
derivative shore plus endpoint reroot, not by a generic strict facet
inheritance theorem.

### 5.2 Even-to-odd union branch

The two bulk sectors are

\[
 \nabla T,qquad y+T.
\tag{5.5}
\]

On a reversed union arm at child depth \(d\ge1\), away from singleton
zero-gaps and the turn collars, the bulk compiler identity is

\[
 P_d^{\operatorname{rev}\nabla T}(\nabla T_i)
 =P_{d-1}(T)_{i+d},
\tag{5.6}
\]

while the marked arm uses \(y+P_d(T)\).  The union arm therefore uses one
lower parent depth, but the marked arm still needs the full child depth.
Singleton zero-gaps and the two turn collars must be excluded or repaired.

The saturating-cycle/Catalan-compression theorem constructs an exact central
path of this parity for every \(r\).  It does not supply SB1--SB4.

### 5.3 Odd-to-odd diamond branch

The bulk sector symbols are

\[
 U=\nabla T,qquad X=x+T,qquad Y=y+T,qquad
 A=xy+\partial T.
\tag{5.7}
\]

For a Catalan-leave gap \(g\), the two new coordinates have one-run length
\(g+1\) and zero-gap length \(2g-1\).  Their biresidence through depths
\((d,u)\) requires

\[
 g\ge d,qquad g\ge\left\lceil\frac{u+2}{2}\right\rceil.
\tag{5.8}
\]

This controls only the two new coordinates on the mixed ribbons.  Old
coordinates on \(U\) use the union event stream, and the all-\(A\) factor is
ordered by the independent factor in (2.2).  Therefore owner-level Catalan
spacing does not imply SB1.

## 6. Protected rerooting as an exact proof route

Let a source chronology be cut into blocks at old cut set \(C\), where a cut
position is the boundary between two consecutive rows, then reordered and
oriented to give \(T'\).  For an old witness interval \([a,b]\), put

\[
 \partial[a,b]=\{a,a+1,\ldots,b-1\},
\]

its set of internal row boundaries, with \(\partial[a,a]=\varnothing\), and
let

\[
 {\cal H}_T(U)=
 \{\partial[a,b]:U=\bigcup_{i=a}^{b}T_i\}
\]

with occurrences retained separately.  Let \(x_{T'}(U)\) count its new
cross-block witnesses.  Then

\[
 m_{T'}(U)=
 \#\{H\in{\cal H}_T(U):H\cap C=\varnothing\}
 +x_{T'}(U).
\tag{6.1}
\]

Put

\[
 {\cal V}_T(C)=
 \{U:C\cap H\ne\varnothing\text{ for every }H\in{\cal H}_T(U)\}.
\]

Thus the reroot is upper-complete exactly when

\[
 {\cal V}_T(C)\subseteq\operatorname{supp}x_{T'}.
\tag{6.2}
\]

### Theorem 6.1 (protected Shadow--Braid closure)

Suppose a block reroot:

1. preserves exact sector ownership and has legal declared seams;
2. satisfies the upper cut/ladder condition (6.2);
3. passes the literal post-reroot residence and chain-alignment tests SB1;
4. transports named pin/common-cap witnesses outside the changed collar and
   recomputes every affected pin, envelope letter, and residual domain
   inside the collar; and
5. the resulting global cap passes SB3--SB4.

Then it satisfies Theorem 4.1.

#### Proof

Clause 1 is SB0, (6.2) is exactly SB2, clause 3 is SB1, and clauses 4--5 are
SB3--SB4.  Apply Theorem 4.1.  \(\square\)

The result is exact but does not assert that a suitable cut set exists.
Upper protection is downward under adding cuts, while residence repair often
requires hitting more short-run hazards.  The two requirements have opposite
monotonicity.

For K16, the c7be endpoint reroot has three blocks of lengths
\(6389,6437,44\).  Every one of the 39,197 old interval values has an
internal witness, so no old upper value is vulnerable; the new seam ladders
install exactly six missing masks.  The subsequent variable schedule,
singleton cap, and common-cap assignment pass SB1, SB3, and SB4.  This is an
exact finite instance of Theorem 6.1.

For the direct K17 four-sector factor, protected rerooting is necessarily
global in the current architecture.  Every direct-formula upper-q1 repair
needs at least 60 factor-external edges, hence at least 61 deleted factor
edges for a Hamilton path.  Independently, the frozen natural factor needs
at least 49 cuts on its 19,170-cycle before the staircase budget can pass.
No bounded local-reroot induction follows.

## 7. Catalan block recursion: proved part and missing part

Two Catalan constructions are already exact.

1. The saturating-cycle construction gives, in every even dimension, an
   exact even-to-odd central path with the correct \((2M-C_r)+2M\) owner
   count and legal Johnson seam.
2. The four-sector theorem gives an odd-to-odd child 2-factor whenever the
   parent is owner-level diamond-ready and the cap-two incidence factor
   exists.

Neither is a Shadow--Braid induction.

The Greene--Kleitman incidence matching supplies every immediate lower and
upper colour once and has exactly \(C_r\) components, but its induced middle
forest branches.  The vertex `010101` already has degree three at semilength
three.  Therefore “add \(C_r\) bridges and obtain a Hamilton braid” is not a
proof.  A Catalan linearization theorem with replacement ledgers is still
open.

Theorems 2.2--2.4 remove one false part of that target.  The \(U\)-deck need
not be linearized by itself.  The forced marginal residual ledger has the
exact edge counts

\[
 AA=XX=YY=M-C_r,\qquad AX=AY=C_r,
\]

but its separated cap-two specialization always seals the \(AA\) factor in
cycles.  The coupled choice (2.21)--(2.22) preserves those counts while
allowing a balanced residual path cover with exactly \(C_r\) endpoints of
each outer tag.  If that coupled graph consists of \(X\)-to-\(Y\) paths, the
Catalan macro spine can connect any compatible \(U\)-path cover with at most
\(C_r-1\) components.  What remains nontrivial is the coupled factor itself,
the endpoint containment/equality matching, joint untagged palette
injection, the protected componentwise pure-old upper ledger, and the other
Shadow--Braid gates.

For the frozen first-occurrence K17 factor, the literal residual graph has
exactly 1,430 open \(X\)-to-\(Y\) paths and 15 sealed \(AA\) cycles, with
cycle-length histogram

\[
 3^9,4^2,6^1,442^1,455^1,4067^1.
\]

Thus its endpoint types are already balanced; the failure is precisely the
uncoupled cap-two cycle bank, containing all 5,005 selected \(A\)-owners.

For K17 a frozen local cyclic matching already realizes the component-neutral
untagged identity with \(c=737\):

\[
 4268\text{ internal}+1474\text{ ports}+693\text{ direct}=6435.
\]

Opening one retained direct gap would give the scalar linear ledger
\(4268+1474+692=6434\).  This artifact does not yet supply the global
residual \(A/X/Y\) chronology, a distinguished authenticated opening, upper
coverage, residence, or a compiler.

The K15 parent is diamond-ready at the owner level, and its cap-two graph has
an integral factor.  Its K17 child factor is lower-rainbow, but its upper-q1
palette has only \(17709/19448\) colours.  Consequently it is **not
regenerative** for the next diamond: an occurrence transversal for all child
rank-\((r+2)\) unions does not exist on that factor.

Call an odd package **regenerative at the optimum length** when it contains,
in addition to an SB0--SB4 certificate of length \(B(2r-1)\), an auxiliary
owner-level diamond-ready factor and the event/port data needed to audit the
next facet and diamond ribbons.  The auxiliary factor need not be the word
chronology, but it must live on the same exact middle deck.

### Hypothesis CSB\(_r\) (protected Catalan Shadow--Braid extension)

Every optimum-length regenerative package in dimension \(2r-1\) admits
simultaneously:

1. an odd-to-even protected braid satisfying SB0--SB4 with physical length
   \(B(2r)\);
2. an odd-to-odd four-sector protected braid satisfying SB0--SB4 with
   physical length \(B(2r+1)\); and
3. the auxiliary factor and event/port data that make clause 2's
   optimum-length certificate regenerative in dimension \(2r+1\).

This is the precise missing Catalan/protected-reroot theorem.  It is stronger
than central ownership, q1 rainbows, residence, or ordinary Hall separately.
It is also an exact terminal existence hypothesis: SB3--SB4 already encode a
simultaneous integral common-cap compiler, and clauses 1--2 already
reconstruct the two child words.

The endpoint-compatible construction of Theorem 2.4 is now the smallest
proved owner/lower-q1 candidate for clause 2.  To become recursive it must
carry its distinguished opening colour and endpoint record into SB3, pass
the componentwise and tagged upper ledgers and SB1--SB4, and regenerate the
auxiliary child factor in clause 3.

## 8. Odd-spine all-\(k\) induction

### Theorem 8.1 (conditional odd-spine induction)

Assume an optimum-length regenerative base package in one odd dimension
\(2r_0-1\), and assume CSB\(_r\) for every \(r\ge r_0\).  Then

\[
 \nu(k)=B(k)
\]

for every \(k\ge2r_0-1\).

#### Proof

The base SB0--SB4 certificate and Theorem 4.1 give the optimum word in
dimension \(2r_0-1\).  Apply CSB\(_{r_0}\).  Theorem 4.1 gives optimal words in dimensions
\(2r_0\) and \(2r_0+1\), and clause 3 supplies the next regenerative odd
package.  Repeat on the odd spine.  At stage \(r\), the even branch gives
dimension \(2r\), while the odd branch gives dimension \(2r+1\) and the
next induction state.  These branches cover every subsequent dimension.
\(\square\)

Theorem 8.1 is a logically valid induction theorem, but CSB\(_r\) is not
proved.  The current finite data locate its first missing pieces rather than
establish it.

## 9. K15/K16/K17 reconciliation

\[
\begin{array}{c|c|c|c}
\text{branch}&\text{owner result}&\text{closed gates}&\text{open/failing gates}\\ \hline
15\to16&\text{two exact shores}&
 \text{upper reroot, residence, pin, common cap}&
 \text{no uniform plateau inheritance}\\
16\to17&\text{fixed occurrence model}&
 \text{individual target intervals}&
 \text{opposite-choice simultaneous upper core}\\
15\to17&\text{four-sector residual ledger, lower q1 exact}&
 \text{owner flow, component-neutral U law}&
 \text{endpoint balance, upper, residence, compiler, regeneration}
\end{array}
\]

The K16 success therefore supports the even branch of an odd-spine
induction.  The four-sector K17 factor is the correct central seed for the
next odd branch, but it does not yet satisfy the Shadow--Braid hypotheses.

## 10. Exact remaining theorem

An unconditional all-\(k\) proof in this architecture must construct, for
every semilength, one common child action that simultaneously supplies:

1. exact Pascal sector ownership, a coupled endpoint-compatible residual path
   factor, and a regenerative diamond-ready auxiliary factor;
2. a protected all-width upper witness ledger after the final braid;
3. a legal P/Q schedule passing the literal run and nonempty-envelope tests;
4. all positional pins after their combined cap, with domains rebuilt; and
5. one global common-cap compiler or a noncircular sufficient certificate
   for it.

Catalan counts prove item 1 only at the owner level.  Protected rerooting is
an exact verification method for items 2--5 once a candidate braid exists.
No theorem presently constructs the common action in every dimension.

## 11. Primary dependencies

- `MATH_THEOREM_MASTER_STAIRCASE_PINNED_COMMON_CAP_COMPILER_20260731.md`.
- `MATH_THEOREM_ODD_EVEN_REROOT_PINNED_COMMON_CAP_COMPILER_20260731.md`.
- `MATH_THEOREM_MONOTONE_DEADLINE_RUN_STAIRCASE_20260731.md`.
- `MATH_AUDIT_MONOTONE_DEADLINE_RUN_STAIRCASE_ARBITRARY_STARTS_20260731.md`.
- `MATH_THEOREM_A_PASCAL_REROOT_CUT_TRANSVERSAL_REDUNDANCY_20260731.md`.
- `MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md`.
- `MATH_THEOREM_AD_K17_K15_FOUR_SECTOR_FACTOR_AND_RETHREAD_GATES_20260731.md`.
- `MATH_THEOREM_AD_K17_FORCED_U_YAX_CATALAN_BRAID_AND_FIXEDU_CSP_20260731.md`.
- `MATH_LEMMA_K17_COMPONENT_NEUTRAL_U_INSERTION_LEDGER_20260731.md`.
- `MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`.

All positive conclusions above are finite or conditional.  No K17 word and
no unconditional all-\(k\) induction is asserted.
