# Second-wave O: direct first-shadow factor attack

Date: 2026-07-24

No web search, finite search, or computational experiment is used in this report.

## Verdict

The requested unconditional exact $C_{2m+1}$-factor theorem is not proved. The attack nevertheless gives a sharp theorem immediately next to the exact-factor fibre:

> **PBBS complete-shadow theorem.** The canonical periodic box-ball cycle factor of $KG(2m+1,m)$ covers every rank-$(m-1)$ angle color, every load is at most $3$, and at most $W/(m+2)$ colors have load outside $\{1,2\}$.

This is an $O(W/m)$ first-shadow result with exact coverage of all middle vertices. It is not yet an exact wreath factor because a PBBS component may have length $\ell(2m+1)$ with $\ell>1$.

The decisive exact-factor reduction is now:

> Find an exact $C_{2m+1}$-factor at edge distance $o(W)$ from PBBS.

The angle histogram is stable enough that this immediately proves the requested theorem. An owner-compatible rainbow skeleton initially leaves fewer than $6B$ centers unretained; after trimming the consecutive long-component runs which violate the immediate owner-phase condition, it leaves fewer than $8B$, where

\[
B=\frac{W}{2m+1}=\operatorname{Cat}_m=o(W),
\]

and asks for a self-reciprocal length-$(2m+1)$ sewing on that leave.

The other routes also sharpen:

- a deterministic PBBS two-sided-rainbow linear forest has only $O(B)$ missing colors and components;
- a complementary-geodesic completion transfers defect by
  \[
  M_1\le 3d+\eta_L+\eta_T;
  \]
- a cyclic total-unimodular flag relaxation gives angle loads in $\{1,2\}$ except on an exponentially small stabilizer-three family and passes every elementary containment cut;
- complete first-shadow coverage inside one literal exact factor is equivalent to a perfect matching in a decorated wreath hypergraph, whose uniform fractional perfect matching is explicit;
- signed integral trades realize the desired correction exactly in the lattice, but positivity remains unproved.

Every unproved statement is marked below. No statement about PBBS, a signed vector, a local wedge assignment, or a partial forest is promoted to an exact wreath factor.

The report imports previously audited theorems: exact odd $C_n$-factors exist; every odd-graph $C_n$ is a wreath; the cyclic parenthesis map is a permutation whose orbit lengths are divisible by $n$ when $\gcd(n,m)=1$; PBBS has componentwise three-state coordinate homomesy; and zero-point-margin lower corrections have rank-isolated integral selector lifts. All new implications and constants are proved here.

## 1. Exact depth-one objective

Put

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\frac{W}{n}=\operatorname{Cat}_m,
\]

and

\[
N=\binom{n}{m-1}=\frac{m}{m+2}W,\qquad
r=W-N=\frac{2W}{m+2}.
\]

For a spanning odd-graph $2$-factor $F$, let $Y_F(X),Z_F(X)$ be the two neighbors of a middle vertex $X$. Its angle is

\[
\chi_F(X)=Y_F(X)\cap Z_F(X)\in\binom{[n]}{m-1}.
\]

Write

\[
\mu_F(S)=\#\{X:\chi_F(X)=S\},
\]

\[
M(F)=\#\{S:\mu_F(S)=0\},\quad
T_2(F)=\#\{S:\mu_F(S)\ge2\}.
\]

Every owner contributes one angle occurrence, so $\sum_S\mu_F(S)=W=N+r$.

### Proposition 1.1: exact load identities

For any nonnegative integral load vector $\mu$ of total $W$, put

\[
P(\mu)=\sum_S(\mu(S)-2)_+.
\]

Then

\[
\boxed{P(\mu)=r+M(\mu)-T_2(\mu).}
\tag{1.1}
\]

Consequently

\[
\boxed{
E_{12}(\mu)
:=\sum_S\operatorname{dist}(\mu(S),\{1,2\})
=r+2M(\mu)-T_2(\mu).
}
\tag{1.2}
\]

For $m\ge3$, the mobile floor/ceiling quota has floor $1$ and exactly $r$ quota-$2$ entries. Its exact overload is

\[
\boxed{
O_1(\mu)=M(\mu)+(r-T_2(\mu))_+.
}
\tag{1.3}
\]

#### Proof

There are $N-M-T_2$ load-one entries and $T_2$ entries of load at least two. Hence

\[
W=(N-M-T_2)+2T_2+P=N-M+T_2+P,
\]

which proves (1.1) and (1.2).

Starting with quota one everywhere, each hole costs one. The $r$ bonus quotas remove one overload unit on at most $\min(r,T_2)$ above-floor targets. Thus

\[
O_1=M+r-\min(r,T_2)=M+(r-T_2)_+.
\]

### Corollary 1.2: equivalent asymptotic targets

As $m\to\infty$,

\[
\boxed{
M(F)=o(W)
\iff O_1(F)=o(W)
\iff
\#\{S:\mu_F(S)\notin\{1,2\}\}=o(W).
}
\tag{1.4}
\]

Indeed,

\[
M\le O_1\le M+r,
\]

and

\[
M
\le \#\{\mu\notin\{1,2\}\}
\le M+\frac{r+M}{2}.
\tag{1.5}
\]

The last bound follows from

\[
\sum_S(\mu(S)-1)_+=r+M,
\]

because every load at least three contributes at least two.

At $m=2$, the floor quota is $2$, not $1$. Formula (1.3) will only be used for $m\ge3$; the PBBS boundary is checked separately.

## 2. Exact centered-edge normal form

For each owner $X\in\binom{[n]}m$, an admissible centered Johnson edge is

\[
e_X=\{Y,Z\},\qquad
Y,Z\in\binom{X^c}{m},\qquad Y\ne Z.
\]

Since $|X^c|=m+1$,

\[
Y\cup Z=X^c,\qquad
Y\cap Z\in\binom{[n]}{m-1}.
\]

Thus the upper color $X^c$ is automatically unique, and the lower color is the proposed angle at $X$.

### Proposition 2.1: exact reciprocity criterion

A family $(e_X)_X$ is the neighbor-pair system of a spanning odd-graph $2$-factor if and only if

\[
\boxed{
Y\in e_X\iff X\in e_Y
\quad\text{for all }X,Y.
}
\tag{2.1}
\]

Under (2.1), join $X$ to the two members of $e_X$. The relation is symmetric and every vertex has degree two. The converse is immediate.

Such a $2$-factor is an exact wreath factor precisely when all its components have length $n$, because every $n$-cycle in the odd graph is a wreath.

The three separate gates are:

1. one admissible centered edge per owner;
2. self-reciprocity (2.1);
3. component length $n$.

The total-unimodular construction in Section 8 solves the first gate with an almost perfect angle histogram. It does not solve the last two.

## 3. Canonical PBBS has complete first shadow

### 3.1 Parenthesis map

Represent $A\in\binom{[n]}m$ by its cyclic binary word. Regard $1$ as an opening step and $0$ as a closing step. Cyclic noncrossing matching leaves one zero unmatched; call it $r_+(A)$. Define

\[
f(A)=A^c\setminus\{r_+(A)\}.
\tag{3.1}
\]

Reverse matching gives $r_-(A)$ and

\[
f^{-1}(A)=A^c\setminus\{r_-(A)\}.
\tag{3.2}
\]

The canonical periodic box-ball theorem gives that $f$ is a permutation, adjacent iterates are disjoint, and its orbits form a spanning odd-graph cycle factor $P_m$. Since $\gcd(n,m)=1$, every orbit length is divisible by $n$. For $m\ge2$, no orbit has length two, so

\[
f(A)\ne f^{-1}(A)
\]

and every PBBS angle has rank $m-1$.

### Theorem 3.1: PBBS complete-shadow and multiplicity-three theorem

For every $m\ge2$ and every $S\in\binom{[n]}{m-1}$,

\[
\boxed{1\le\mu_P(S)\le3.}
\tag{3.3}
\]

#### Lower bound

The cyclic word of $S$ has three unmatched zeros. Cut there and write

\[
0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,
\tag{3.4}
\]

where each $D_i$ is a Dyck word, possibly empty. At least one has positive height.

Choose $D_i$ of maximal height, and let $u$ be the down-step after its rightmost maximum. Flip $u$ from zero to one. The modified block has excess $+2$, whose opens consume $z_{i+1}$ and $z_{i+2}$, leaving $z_i$ unmatched. Therefore

\[
r_+(S\cup\{u\})=z_i.
\tag{3.5}
\]

Now flip $z_i$ instead and rotate the word as

\[
1D_i\,0D_{i+1}\,0D_{i+2}.
\tag{3.6}
\]

The maximum prefix heights in its three regions are bounded by

\[
1+H(D_i),\qquad H(D_{i+1}),\qquad H(D_{i+2})-1.
\]

The global maximum therefore lies strictly in the first region, and its rightmost occurrence is followed by $u$. In a word of total height $-1$, the reverse-unmatched zero is the down-step after the rightmost global maximum. Hence

\[
r_-(S\cup\{z_i\})=u.
\tag{3.7}
\]

Let $T=[n]\setminus S$ and $X=T\setminus\{u,z_i\}$. Equations (3.1), (3.2), (3.5), and (3.7) give

\[
f(S\cup\{u\})=X,\qquad
f^{-1}(S\cup\{z_i\})=X.
\]

Thus

\[
S\cup\{u\}\longrightarrow X\longrightarrow S\cup\{z_i\}
\]

is a directed PBBS two-path whose angle is $S$. This proves $\mu_P(S)\ge1$.

For $m=2$, exactly one block in (3.4) is $10$, so the same proof applies.

#### Upper bound

For $u\in T=[n]\setminus S$, define

\[
\alpha_S(u)=r_+(S\cup\{u\}),\qquad
\beta_S(u)=r_-(S\cup\{u\}).
\tag{3.8}
\]

Let $U_+(S)$ and $U_-(S)$ be the three forward and reverse unmatched-zero sets. The deficit-three clean-label argument gives

\[
\alpha_S(T)\subseteq U_+(S),\qquad
\beta_S(T)\subseteq U_-(S).
\tag{3.9}
\]

Indeed, flipping a zero inside a Dyck block creates two excess opens which consume the next two displayed unmatched zeros. Flipping one displayed unmatched zero instead removes that zero and creates one open, which consumes the next displayed unmatched zero. In either case the third old unmatched zero remains. Reversing the word proves the second inclusion.

An angle occurrence directed as

\[
S\cup\{u\}\longrightarrow X\longrightarrow S\cup\{v\}
\]

is equivalent to

\[
\alpha_S(u)=v,\qquad \beta_S(v)=u.
\tag{3.10}
\]

Occurrences are therefore in bijection with fixed points of $\beta_S\circ\alpha_S$. Every fixed point lies in $\beta_S(T)\subseteq U_-(S)$, a set of size three. The predecessor $u$ determines

\[
X=T\setminus\{u,\alpha_S(u)\},
\]

so there is no double counting. Hence $\mu_P(S)\le3$.

### Corollary 3.2: exact PBBS defect

Let

\[
a_j=\#\{S:\mu_P(S)=j\},\qquad 1\le j\le3.
\]

Then

\[
a_1+a_2+a_3=N,\qquad
a_1+2a_2+3a_3=W,
\]

and hence

\[
\boxed{
a_2+2a_3=r=\frac{2W}{m+2}.
}
\tag{3.11}
\]

In particular,

\[
\boxed{
a_3\le\frac{W}{m+2}=O(W/m).
}
\tag{3.12}
\]

There are no holes and no loads above three, so $a_3$ is exactly the number of loads outside $\{1,2\}$.

For $m\ge3$, (1.3) and (3.11) give

\[
\boxed{O_1(P_m)=a_3.}
\tag{3.13}
\]

At $m=2$, the unique balanced quota is identically two. Conservation gives $a_1=a_3$, and

\[
O_1(P_2)=\frac12\|\mu_P-2\mathbf1\|_1=a_3.
\]

This separate calculation is required; using floor one at $m=2$ would be false.

### Scope

$P_m$ is a genuine spanning $2$-factor, but its components may have length $\ell n$ with $\ell>1$. Theorem 3.1 is not an exact wreath-factor theorem.

## 4. Sparse rebundling stability

For spanning $2$-factors $F,G$ on the same vertices, put

\[
t=|E(F)\setminus E(G)|=|E(G)\setminus E(F)|.
\]

### Theorem 4.1: angle stability

If $F=P_m$, then

\[
\boxed{\|\mu_G-\mu_P\|_1\le4t,}
\tag{4.1}
\]

\[
\boxed{M(G)\le2t,}
\tag{4.2}
\]

\[
\boxed{
\#\{S:\mu_G(S)\notin\{1,2\}\}
\le\frac{W}{m+2}+4t,
}
\tag{4.3}
\]

and, for $m\ge3$,

\[
\boxed{
O_1(G)\le\frac{W}{m+2}+2t.
}
\tag{4.4}
\]

#### Proof

An angle changes only at a vertex incident with a removed $P_m$ edge. There are at most $2t$ such vertices. Replacing one occurrence changes the histogram by $L^1$-distance at most two, proving (4.1).

PBBS covers every target, so each hole of $G$ consumes a changed PBBS occurrence, proving (4.2). Outside the $a_3$ PBBS load-three targets, every new bad target costs at least one unit of histogram $L^1$-distance. Equations (3.12) and (4.1) prove (4.3).

Mobile overload is one half of the $L^1$-distance to the set of balanced floor/ceiling vectors. Distance to a fixed set is $1$-Lipschitz, so

\[
O_1(G)\le O_1(P_m)+\frac12\|\mu_G-\mu_P\|_1,
\]

which gives (4.4).

### Theorem 4.2: exact rebundling lower bound

Let $b_1(P_m)$ be the number of level-one PBBS components, and let $L_{\mathrm{long}}(P_m)$ be the number of vertices on PBBS components longer than $n$. For every exact $C_n$-factor $G$,

\[
\boxed{
|E(P_m)\setminus E(G)|
\ge B-b_1(P_m)
=\frac{L_{\mathrm{long}}(P_m)}{n}.
}
\tag{4.5}
\]

#### Proof

Delete the $t=|E(P_m)\setminus E(G)|$ old edges. Every untouched PBBS component remains a whole component of $G$, so it must already have length $n$; there are at most $b_1(P_m)$ such components. A PBBS cycle cut $s\ge1$ times gives exactly $s$ residual paths. Hence the graph of retained old edges has at most

\[
b_1(P_m)+t
\]

components. Adding the $t$ new edges cannot increase component count, while $G$ has exactly $B$ components. Thus $B\le b_1(P_m)+t$.

If the PBBS component levels are $\ell_j$, then

\[
B=\sum_j\ell_j
=b_1(P_m)+\frac{L_{\mathrm{long}}(P_m)}n,
\]

proving the second equality.

Thus Catalan-scale edge change is intrinsically necessary when most PBBS mass lies in long components. No asymptotic bound on $b_1(P_m)$ is proved here.

### UNPROVED O2-A: sparse PBBS rebundling

There exists an exact $C_n$-factor $G_m$ such that

\[
\boxed{
|E(P_m)\setminus E(G_m)|=o(W).
}
\tag{O2-A}
\]

O2-A and Theorem 4.1 imply the requested exact-factor theorem.

The scale $O(B)$ is sufficient because $B=W/n=o(W)$. Component-count potential arguments allow an $\Omega(B)$ lower bound on local splitting operations, but that scale does not obstruct O2-A. The missing result is a positive supply and compatible routing theorem for balanced switches.

## 5. Omitted-label balance

Every odd-graph edge $XY$ has omitted label

\[
\lambda(XY)=[n]\setminus(X\cup Y).
\]

### Theorem 5.1: every spanning $2$-factor is globally label-balanced

If $t_a$ is the number of selected edges labelled $a$, then

\[
\boxed{t_a=B\quad\text{for every }a\in[n].}
\tag{5.1}
\]

#### Proof

An edge labelled $a$ has neither endpoint containing $a$; every other edge has exactly one such endpoint. Hence $W-t_a$ is the selected-edge endpoint incidence at $a$. It is also

\[
2\binom{n-1}{m-1}=2mB=(n-1)B.
\]

Since $W=nB$, one gets $t_a=B$.

In an exact factor, the $B$ copies of each label are distributed one per $C_n$ component. The imported three-state PBBS homomesy theorem gives the componentwise strengthening: a PBBS component of length $\ell n$ uses each omitted label $\ell$ times. The unresolved operation is therefore componentwise splitting, not global label balancing.

## 6. Owner-compatible PBBS rainbow skeleton

For each PBBS center $X$, define

\[
e_X=\{f^{-1}(X),f(X)\}.
\tag{6.1}
\]

Its lower color is $\chi_P(X)$ and its upper color is $X^c$. Let $J_P$ be the graph containing all $e_X$.

### Proposition 6.1: PBBS step-two graph

$J_P$ is $2$-regular and has at most $2B$ cycles.

#### Proof

The only centered edges containing a vertex $Y$ are $e_{f(Y)}$ and $e_{f^{-1}(Y)}$. On an $f$-cycle $v_i$, one has

\[
e_{v_i}=v_{i-1}v_{i+1}.
\]

Thus one PBBS cycle gives $\gcd(2,L)\le2$ step-two cycles. There are at most $B$ PBBS cycles because their levels sum to $B$.

### Theorem 6.2: Catalan-defect centered rainbow forest

There is a centered PBBS edge set

\[
\mathcal P=\{e_X:X\in A\}
\]

which is a spanning linear forest and, for some $d\le2B$, satisfies

\[
|A|=N-d,
\tag{6.2}
\]

\[
\boxed{
\begin{aligned}
\text{missing lower colors}&=d\le2B,\\
\text{missing upper colors}&=r+d<6B,\\
\text{forest components}&=r+d<6B.
\end{aligned}}
\tag{6.3}
\]

All retained lower colors are distinct, all retained upper colors are distinct, and every edge retains its literal PBBS owner.

#### Proof

For every lower target $S$, choose one center $X_S$ with $\chi_P(X_S)=S$, possible by Theorem 3.1. These $N$ centered edges have distinct lower colors and distinct upper colors.

The selected graph is a subgraph of the $2$-regular graph $J_P$. Delete one edge from every surviving cycle. At most $2B$ edges are deleted. The resulting forest has $N-d$ edges on $W$ vertices, hence $W-(N-d)=r+d$ components. The same quantity is the number of missing upper colors. Finally

\[
\frac rB=\frac{2n}{m+2}<4,
\]

so $r+d<6B$.

### Exact residual extension criterion

Let

\[
U=\binom{[n]}m\setminus A.
\]

Retaining $e_X$ for $X\in A$ retains both incident PBBS odd edges. A missing center $y\in U$ therefore has residual degree demand

\[
d_U(y)=2-\#\{x\in A:y\in e_x\}.
\tag{6.4}
\]

The retained wedges extend to a self-reciprocal spanning $2$-factor if and only if the induced odd graph $KG(n,m)[U]$ contains a subgraph with degree sequence $d_U$. Adding that residual $f$-factor to the forced PBBS edges proves sufficiency; reciprocity proves necessity. Exact wreath packaging additionally requires every completed component to have length $n$.

This shows why ordinary Johnson forest completion is insufficient. If $U$ is badly scattered along PBBS cycles, forced cross-boundary edges can consume all residual degree and force the PBBS pairing back.

### Phase obstruction

An untrimmed PBBS Johnson path cannot always survive inside a new exact factor.

In an oriented exact odd $n$-cycle, let $\tau$ be the step-two Johnson successor and $\sigma$ the odd successor. Since

\[
2(m+1)\equiv1\pmod n,
\]

one has $\sigma=\tau^{m+1}$. Hence, in the oriented Johnson row

\[
V_0,V_1,\ldots,V_{n-1},
\]

the owner of the edge $V_jV_{j+1}$ is exactly $V_{j+m+1}$, and

\[
V_{j+m+1}=[n]\setminus(V_j\cup V_{j+1}).
\tag{6.5a}
\]

Let $X_i=f^i(X_0)$. In the PBBS step-two graph, the centered edge

\[
e_{X_i}=\{X_{i-1},X_{i+1}\}
\]

has owner $X_i$. Here consecutive step-two edges mean

\[
e_{X_i},e_{X_{i\pm2}},e_{X_{i\pm4}},\ldots
\]

along a component of $J_P$. Suppose $m+1$ such consecutive edges occur, in either orientation, in an exact self-colored Johnson $n$-cycle. For the first edge, exact ownership puts its owner at Johnson offset $m+1$. In the forward orientation this forces

\[
X_i=X_{i+n};
\]

in the reverse orientation it forces $X_i=X_{i-n}$. Either identity says that the PBBS orbit length divides $n$. It is impossible on a PBBS component of level greater than one.

Thus every common Johnson path on a long PBBS component has at most $m$ edges. This is a genuine owner-phase obstruction, not a lower/upper rainbow obstruction.

### Corollary 6.3: phase-trimmed skeleton

The forest of Theorem 6.2 can be further trimmed so that every retained path has at most $m$ edges. If $\delta$ is the total number of deleted lower colors, then

\[
\boxed{\delta<4B.}
\tag{6.5}
\]

The resulting number of missing owners and forest components is

\[
u=W-(N-\delta)=r+\delta<8B.
\tag{6.6}
\]

#### Proof

On every forest path of $L$ edges, delete $\lfloor L/(m+1)\rfloor$ well-spaced edges. The number of added deletions is less than

\[
\frac{W}{m+1}<2B.
\]

Together with the at most $2B$ cycle-breaking deletions, this gives (6.5). Equation (6.6) follows from $r<4B$.

### UNPROVED O2-B: anchored self-colored sewing

The occurrence representatives, cycle-breaking edges, and phase-trimming edges can be chosen so that the resulting phase-trimmed centered forest admits a reciprocal completion preserving all retained owner pairs, and every completed component has length $n$.

If O2-B holds, the exact factor retains one occurrence of each of $N-\delta$ distinct lower colors. Therefore

\[
M\le\delta<4B.
\]

All other angle occurrences come from the $u<8B$ unretained owners. Each load at least three consumes at least two additions beyond the retained load-one baseline. Hence

\[
\boxed{
\#\{S:\mu(S)\notin\{1,2\}\}
\le\delta+\frac u2<8B.
}
\tag{6.7}
\]

For $m\ge3$, choose any balanced quota vector $b$ dominating the retained $0/1$ baseline. Both the completed excess and $b$ minus that baseline are nonnegative vectors of mass $u$. Thus

\[
\boxed{O_1\le\frac12\|\mu-b\|_1\le u<8B.}
\tag{6.8}
\]

O2-B is a literal exact-middle theorem at the Catalan target scale. Theorem 4.2 proves that this scale is necessary if $b_1(P_m)=o(B)$, but that hypothesis is unproved. The phase trimming removes the immediate offset contradiction for retained consecutive PBBS runs; it is not claimed necessary for every possible sewing architecture. The residual $f$-factor and cycle-length conditions remain unproved.

### Orientation-preserving sewing normal form

There is also an exact restricted-permutation formulation of sparse PBBS rebundling.

Orient every PBBS component by $f$. Choose a set $C$ of cut tails, remove the arcs

\[
c\longrightarrow f(c),\qquad c\in C,
\]

and let

\[
\nu(c)=f^{k(c)}(c)
\]

be the next cut tail on the same PBBS orbit. The resulting segment

\[
P_c=(f(c),f^2(c),\ldots,\nu(c))
\]

has $k(c)$ vertices. The map $\nu$ is a permutation of $C$.

For a permutation $\pi$ of $C$, insert seams

\[
c\longrightarrow f(\pi(c)).
\tag{6.9}
\]

### Theorem 6.4: exact legal-sewing criterion

The seams (6.9) are odd-graph edges if and only if, for every $c\in C$, with $d=\pi(c)$,

\[
\boxed{
c=d
\quad\text{or}\quad
c=d\setminus\{x\}\cup\{r_+(d)\}
\text{ for a unique }x\in d.
}
\tag{6.10}
\]

In the diagonal case the seam label is $r_+(d)$; in the nontrivial case it is $x$.

The new cycles are indexed by cycles of

\[
\boxed{\theta=\pi\circ\nu}
\tag{6.11}
\]

on the segment labels $C$. A $\theta$-cycle $\mathcal C$ gives a factor cycle of length

\[
\boxed{
\sum_{c\in\mathcal C}k(c).
}
\tag{6.12}
\]

Consequently this orientation-preserving sewing is an exact wreath factor if and only if every untouched PBBS component has length $n$ and every $\theta$-cycle has weight $n$.

#### Proof

Since

\[
f(d)=d^c\setminus\{r_+(d)\},
\]

the seam $c\to f(d)$ is legal exactly when

\[
c\subseteq d\cup\{r_+(d)\}.
\]

Both $c$ and $d$ have size $m$, giving precisely the alternatives (6.10). Directly taking the union with $f(d)$ gives the stated omitted seam label.

After traversing segment $P_d$, one ends at $\nu(d)$. Its new seam enters the segment

\[
P_{\pi(\nu(d))}=P_{\theta(d)}.
\]

Thus segment labels follow $\theta$, and their vertex counts add as in (6.12).

On every resulting length-$n$ cycle, if $t_x$ counts retained PBBS edges labelled $x$ and $a_x$ counts new seams labelled $x$, the shortest-cycle label theorem forces

\[
\boxed{t_x+a_x=1\quad(x\in[n]).}
\tag{6.13}
\]

Thus each final packet is literally rainbow: retained segment-label sets are disjoint and seam labels form their complement.

This normal form does not solve O2-A. It reduces one natural orientation-preserving version to choosing $o(W)$ cut tails and a legal exchange permutation $\pi$ whose weighted cycles all have weight $n$ and whose seam labels complete each packet. Componentwise PBBS homomesy and global label balance do not supply that restricted weighted permutation.

## 7. Complementary-geodesic route

Fix $z\in[n]$, put $Q=[n]\setminus\{z\}$, and write

\[
V=\binom{2m}{m}=(m+1)B.
\]

Cutting a wreath at its unique odd edge labelled $z$ gives, up to reversal, a complementary Johnson geodesic

\[
X_0,X_1,\ldots,X_m\in\binom Qm,\qquad X_m=Q\setminus X_0.
\tag{7.1}
\]

Put

\[
S_i=X_{i-1}\cap X_i,\qquad
U_i=X_{i-1}\cup X_i,\qquad 1\le i\le m.
\]

The corresponding middle vertices containing $z$ are

\[
\{z\}\cup(Q\setminus U_i).
\]

The first-shadow colors are:

- the $m$ internal meets $S_i$;
- the caps $Q\setminus U_1$ and $Q\setminus U_m$;
- the $m-1$ turns
  \[
  \{z\}\cup(Q\setminus\kappa_i),
  \qquad \kappa_i=U_i\cup U_{i+1}.
  \tag{7.2}
  \]

Thus path vertices and upper edge colors must partition their layers, while internal meets and turns must be nearly surjective.

### 7.1 Complementary-geodesic hypergraph

Let

\[
\mathcal M=\binom Qm,\qquad
\mathcal L=\binom Q{m-1},\qquad
\mathcal U=\binom Q{m+1}.
\]

For each unoriented complementary $m$-geodesic, make one hyperedge containing its $m+1$ middle vertices, its $m$ meets, and its $m$ unions. This is a $(3m+1)$-uniform hypergraph $\mathscr G_m$.

### Theorem 7.1: exact regularity

$\mathscr G_m$ is regular of degree

\[
\boxed{
D=\frac{m+1}{2}(m!)^2.
}
\tag{7.3}
\]

Uniform weight $1/D$ is therefore a fractional perfect matching on all three resource classes. An integral matching of $B$ hyperedges saturates every resource and gives an exact wreath factor with perfect internal meet colors.

#### Proof

A directed complementary geodesic is determined by its initial $m$-set, an order for removing its $m$ points, and an order for inserting the $m$ points of its complement. There are $V(m!)^2$ directed paths and $V(m!)^2/2$ unoriented paths. Double counting middle incidences gives

\[
\frac{[V(m!)^2/2](m+1)}{V}
=\frac{m+1}{2}(m!)^2.
\]

Also

\[
|\mathcal L|=|\mathcal U|=\frac{m}{m+1}V,
\]

and every path uses $m$ resources from each of these classes, giving the same degree.

### Theorem 7.2: local extension count

A fixed directed Johnson geodesic of length $\ell$ occurs as a contiguous segment in exactly

\[
\boxed{
(m-\ell+1)(m-\ell)!^2
}
\tag{7.4}
\]

directed complementary $m$-geodesics.

#### Proof

Let the segment run from $X$ to $Y$, and put

\[
D_0=X\setminus Y,\quad E_0=Y\setminus X,\quad
C=X\cap Y,\quad R=Q\setminus(X\cup Y).
\]

Then $|D_0|=|E_0|=\ell$ and $|C|=|R|=m-\ell$. If the segment begins at position $s$, choose the $s$ common points removed before it and the $s$ outside points inserted before it. This gives

\[
\binom{m-\ell}{s}^2(s!)^2((m-\ell-s)!)^2
=(m-\ell)!^2
\]

completions for each $s$. Sum over $0\le s\le m-\ell$.

### Corollary 7.3: exact middle-pair codegrees

If $X,Y\in\mathcal M$ have Johnson distance $\ell\ge1$, then

\[
\deg_{\mathscr G_m}(X,Y)
=(m-\ell+1)(\ell!)^2((m-\ell)!)^2
\tag{7.5}
\]

and

\[
\boxed{
\frac{\deg(X,Y)}{D}
=\frac{2(m-\ell+1)}
{(m+1)\binom m\ell^2}.
}
\tag{7.6}
\]

The maximum is $2/(m+1)$, attained at complementary pairs. Local extension is perfectly regular, but the uniformity grows linearly with $m$ and this normalized codegree is only of order $1/m$; a routine fixed-uniformity nibble does not give the exact matching.

Under the uniform fractional matching, every rank-$(m+2)$ turn target has load

\[
\frac{B(m-1)}{\binom{2m}{m+2}}
=\frac{m+2}{m}\in[1,2].
\tag{7.7}
\]

So turns are fractionally balanced as well.

### Theorem 7.4: geodesic completion transfer

Let $\mathcal F$ be a spanning linear forest on $\mathcal M$, every component a Johnson geodesic. Suppose

\[
|E(\mathcal F)|=mB-d
\]

and its upper colors are distinct. Define

\[
\eta_L
=|E(\mathcal F)|
-\#\{X\cap Y:XY\in E(\mathcal F)\}.
\]

At each degree-two vertex, let $\kappa_X$ be the union of its two incident upper colors, and put

\[
\eta_T
=\#\{X:\deg_{\mathcal F}X=2\}
-\#\{\kappa_X:\deg_{\mathcal F}X=2\}.
\]

Suppose the $d$ missing upper colors can be assigned $d$ Johnson edges which sequentially join distinct component endpoints and leave a geodesic forest. Then the completed graph consists of $B$ complementary paths of length $m$, reconstructs one exact wreath factor $F$, and

\[
\boxed{
M(F)\le3d+\eta_L+\eta_T.
}
\tag{7.8}
\]

#### Proof

Initially there are

\[
V-(mB-d)=B+d
\]

components. After $d$ joins there are $B$ components and $mB$ total edges. A geodesic in $J(2m,m)$ has length at most $m$, so all $B$ components must have length exactly $m$ and complementary endpoints. Distinct upper colors fill the upper layer, giving an exact factor.

The old forest has at least $mB-d-\eta_L$ distinct meets, so its final internal-meet deficit is at most $d+\eta_L$. Each connector creates at most two new degree-two vertices, making the turn deficit at most $2d+\eta_T$. Caps only add coverage. Summing gives (7.8).

### UNPROVED O2-C: geodesic rainbow connector

There are spanning geodesic forests with

\[
d+\eta_L+\eta_T=o(V)
\]

whose missing upper colors admit the completion in Theorem 7.4.

The generic two-sided-rainbow forest does not prove O2-C: it need not be geodesic, need not have complementary endpoints, and does not control turns. The PBBS skeleton has $O(B)$ color defect but is also generally nongeodesic.

## 8. Equivariant total-unimodular flag relaxation

Let $\rho$ cyclically rotate $[n]$. Define the exceptional lower family

\[
\mathcal E
=\left\{
S\in\binom{[n]}{m-1}:
S\text{ is fixed by the order-three subgroup of }\langle\rho\rangle
\right\}.
\]

It is empty unless $3\mid n$. When nonempty,

\[
\boxed{
|\mathcal E|
=\binom{n/3}{(m-1)/3}
\le(n+1)2^{-2n/3}W
=o(W).
}
\tag{8.1}
\]

### Theorem 8.1: equivariant facet SDR

For every $m\ge2$, there is a $\rho$-equivariant map

\[
f_0:\binom{[n]}m\longrightarrow\binom{[n]}{m-1},
\qquad f_0(X)\subset X,
\tag{8.2}
\]

whose fiber vector $q(S)=|f_0^{-1}(S)|$ satisfies

\[
\boxed{
q(S)\in\{1,2\}\quad(S\notin\mathcal E),\qquad
q(S)=0\quad(S\in\mathcal E).
}
\tag{8.3}
\]

It has exact point margins

\[
\sum_{S\ni a}q(S)=(m-1)B
\tag{8.4}
\]

and satisfies every containment cut

\[
\boxed{
\sum_{S\in\mathcal A}q(S)
\le|\partial^+\mathcal A|
\quad
\left(\mathcal A\subseteq\binom{[n]}{m-1}\right).
}
\tag{8.5}
\]

For $m\ge3$,

\[
\boxed{O_1(q)=|\mathcal E|.}
\tag{8.6}
\]

#### Proof

Middle sets have free cyclic orbits because $\gcd(n,m)=1$. A lower stabilizer has order dividing

\[
\gcd(n,m-1)=\gcd(n,3),
\]

so the only nonfree lower sets are $\mathcal E$. A middle set contains at most one exceptional facet: two such facets would have an invariant two-element symmetric difference, impossible under an order-three action.

Delete exceptional lower vertices from the rank-$(m-1,m)$ incidence graph and take the cyclic quotient. A middle-orbit vertex has free-facet degree $d_X\in\{m-1,m\}$; a free lower-orbit vertex has degree $m+2$. Weight each incident edge at $X$ by $1/d_X$. Middle sums are one, and free lower sums lie in

\[
\left[\frac{m+2}{m},\frac{m+2}{m-1}\right]\subseteq[1,2].
\]

When exceptional facets occur, $m\ge4$; otherwise the sum is exactly $(m+2)/m$, including $m=2,3$.

After negating one bipartition, the quotient constraint matrix is a directed bipartite node-edge incidence matrix, hence totally unimodular. Integral lower and upper bounds give an integral quotient solution, which lifts to (8.2)-(8.3).

Cyclic transitivity gives (8.4). The selected preimages of targets in $\mathcal A$ are distinct middle extensions, proving (8.5). If $h$ free targets have load two, then

\[
W=(N-|\mathcal E|)+h,
\qquad h=r+|\mathcal E|,
\]

and (1.3) gives (8.6).

### Theorem 8.2: literal local owner flags

There is a $\rho$-equivariant inclusion bijection

\[
g:\binom{[n]}m\longrightarrow\binom{[n]}{m+1},
\qquad X\subset g(X).
\tag{8.7}
\]

For each $X$, put

\[
U_X=g(X),\qquad S_X=f_0(X),\qquad C_X=[n]\setminus U_X.
\]

Write

\[
U_X\setminus X=\{a_X\},\qquad X\setminus S_X=\{b_X\},
\]

and set

\[
Y_X=S_X\cup\{a_X\}.
\tag{8.8}
\]

Then

\[
C_X-X-Y_X
\]

is a literal odd-graph wedge centered at owner $C_X$, with angle $S_X$. The owners $C_X$ exhaust the middle layer once; the distinguished neighbors $X$ do likewise; and the angle histogram is $q$.

Every coordinate occurs in exactly $2B$ pair labels

\[
D_X=U_X\setminus S_X:
\]

\[
\boxed{
\#\{X:c\in D_X\}
=\binom{n-1}m-(m-1)B
=2B.
}
\tag{8.9}
\]

#### Proof

Ranks $m$ and $m+1$ consist of free cyclic orbits. Their quotient inclusion graph is an $(m+1)$-regular bipartite multigraph with $B$ vertices per side, so it has a perfect matching, which lifts to $g$.

The containments $S_X\subset X\subset U_X$ have successive rank difference one. Hence

\[
X=S_X\cup\{b_X\},\quad
Y_X=S_X\cup\{a_X\},\quad
X\cup Y_X=U_X=C_X^c.
\]

This proves the wedge claim. Equation (8.9) subtracts the exact lower point margin from the complete upper-layer point degree.

### Exact missing equations

Define

\[
\sigma(C_X)=X,\qquad \tau(C_X)=Y_X.
\]

$\sigma$ is a permutation; $\tau$ need not be. The equation

\[
\boxed{
\tau(C)=\sigma^{-1}(C)
\quad\text{for every }C.
}
\tag{8.10}
\]

is sufficient to glue the flags into the directed cycle cover $\sigma$, with angle vector exactly $q$. It becomes an exact wreath factor when every $\sigma$-cycle has length $n$.

Conversely, suppose the flags form an exact factor whose components all have the odd length $n$. On one undirected $n$-cycle, a bijective choice $\sigma(C)$ of one neighbor at every vertex cannot decompose into directed $2$-cycles, because an odd cycle has no perfect matching. Hence it must orient the whole cycle, and its other neighbor is $\sigma^{-1}(C)$. Thus (8.10) is also necessary for the desired exact factor.

For a general $2$-factor with even components, self-reciprocity (2.1) can hold without (8.10): the distinguished choices may form directed $2$-cycles. This distinction does not weaken O2-D, which asks specifically for odd $n$-cycles.

Correct point margins, the coordinate pair-label degrees (8.9), and all cuts (8.5) do not imply (8.10). Thus this is an integral local-owner relaxation, not a factor theorem.

### UNPROVED O2-D: reciprocal flag completion

The maps $f_0,g$ can be chosen so that (8.10) holds and every $\sigma$-cycle has length $n$.

O2-D would give an exact factor with bad first-shadow set contained in the exponentially small family $\mathcal E$.

## 9. Integral trades: lattice versus positivity

Let $\Omega_m$ be the unoriented wreath columns, $A_m$ their middle incidence, and $A_{m-1}$ their first-shadow incidence. Fix an exact factor $F$ with indicator $x_F$.

### Theorem 9.1: signed rank-isolated realization

For $m\ge3$ and the target $q$ of Theorem 8.1, there is $z\in\mathbb Z^{\Omega_m}$ satisfying

\[
\boxed{
A_mz=0,\qquad
A_{m-1}z=q-\mu_F.
}
\tag{9.1}
\]

The lift may be taken rank-isolated from the other proper lower ranks covered by the audited selector construction.

#### Proof

$q$ and $\mu_F$ have the same total and point margins. Therefore

\[
q-\mu_F\in\ker_{\mathbb Z}U_{m-1}.
\]

The integral rectangle-lattice theorem gives

\[
\ker_{\mathbb Z}U_{m-1}
=\left\langle
e_{Kac}-e_{Kbc}-e_{Kad}+e_{Kbd}
\right\rangle_{\mathbb Z}.
\tag{9.2}
\]

Each rectangle has a coefficient-one Petr--Turek selector lift in $\ker_{\mathbb Z}A_m$, vanishing at the other lower ranks. Summing the lifts proves (9.1).

The signed endpoint $x_F+z$ need not be nonnegative. This is the entire missing factor condition.

### UNPROVED O2-E: positive first-shadow lift

\[
\boxed{
\min_{G\text{ exact wreath factor}}
\|\mu_G-q_m\|_1=o(W).
}
\tag{O2-E}
\]

If O2-E holds, then

\[
\#\{S:\mu_G(S)\notin\{1,2\}\}
\le|\mathcal E|+\|\mu_G-q_m\|_1=o(W).
\]

In the equality case, a nonnegative integral $x_F+z$ is automatically $0/1$ because its middle incidence is $\mathbf1$. Signed saturation alone does not provide it. Selector cells are not packing-compatible factor trades, and Graver descent needs a better positive endpoint before it can produce a legal descent step.

## 10. Rainbow core inside one exact factor

For a wreath $C$, let $\partial_1C$ be its $n$ distinct first-shadow intervals.

### Theorem 10.1: exceptional rainbow core

Suppose an exact factor splits as

\[
F=P\sqcup E,\qquad |E|=b,
\]

and the families $\partial_1C$, $C\in P$, are pairwise disjoint. Then

\[
\boxed{M(F)\le nb-r}
\tag{10.1}
\]

and

\[
\boxed{
\#\{S:\mu_F(S)\notin\{1,2\}\}
\le\frac r2+\frac32(nb-r).
}
\tag{10.2}
\]

#### Proof

The rainbow core covers $n(B-b)=W-nb$ distinct lower targets. At most

\[
N-(W-nb)=nb-r
\]

remain uncovered. Apply (1.5).

Set

\[
g_0=\left\lfloor\frac Nn\right\rfloor,\qquad
b_0=B-g_0=\left\lceil\frac{2B}{m+2}\right\rceil,
\]

and let $h=N-ng_0$. Since

\[
\gcd(n,m-1)=\gcd(n,3)
\]

and

\[
n\binom{n-1}{m-2}=(m-1)N,
\]

$N$ is divisible by $n/\gcd(n,3)$. Hence

\[
\boxed{
h\in\{0,n/3,2n/3\},
}
\tag{10.3}
\]

with nonzero cases only when $3\mid n$.

An exact factor containing a rainbow core of size $g_0$ therefore satisfies

\[
\boxed{
\#\{\mu_F\notin\{1,2\}\}
\le\frac{W}{m+2}+n
=O(W/m).
}
\tag{10.4}
\]

The shadow leave of size $h$ is necessarily $(m-1)h/n$-regular. This is not an abstract design obstruction: whenever

\[
0\le h\le\binom nk,\qquad n\mid kh,
\]

a simple $k$-uniform regular family of $h$ sets exists. Minimize the sum of squared point degrees among all such $h$-edge families; any degree gap at least two permits a one-point exchange lowering the sum, so all degrees equal their integral average.

### UNPROVED O2-F: maximal rainbow reservoir

One exact factor contains $g_0=\lfloor N/n\rfloor$ wreaths with pairwise disjoint first shadows.

The symmetric fractional packing exists. What is unproved is that its middle leave decomposes into the remaining $b_0$ wreaths in the same exact factor.

## 11. Decorated-wreath exact matching

Create three resource classes:

1. one vertex for every middle set;
2. one core vertex $c_S$ for every lower target $S$;
3. exactly $r=W-N$ generic labelled bonus tokens.

For a wreath, mark an arbitrary subset of its $n$ distinct first-shadow occurrences. Unmarked $S$ uses $c_S$; marked positions receive distinct bonus tokens. A decorated edge contains the wreath's $n$ middle vertices and its $n$ shadow-side resources, so it is $2n$-uniform.

For $m\ge2$, one has $r\ge n$ (equality at $m=2$), so every marked subset admits such an injection. Equivalently, $r/n=2B/(m+2)\ge1$; the inequality follows from $B=\operatorname{Cat}_m\ge(m+2)/2$.

### Theorem 11.1: exact equivalence

\[
\boxed{
\begin{array}{c}
\text{decorated hypergraph has a perfect matching}\\
\Updownarrow\\
\text{one exact wreath factor has complete first shadow.}
\end{array}}
\tag{11.1}
\]

#### Proof

There are

\[
W+N+r=2W
\]

resources, so a perfect matching has $B$ decorated wreaths. Covering all middle resources gives an exact factor, and covering every core $c_S$ gives complete shadow.

Conversely, in a complete-shadow exact factor choose one occurrence of every $S$ as its core occurrence. Exactly $W-N=r$ occurrences remain; biject them with the bonus tokens.

Complete shadow already implies

\[
\#\{S:\mu(S)\ge3\}
\le\frac r2
=\frac{W}{m+2}.
\tag{11.2}
\]

### Theorem 11.2: explicit fractional perfect matching

The decorated hypergraph has an exact uniform fractional perfect matching.

#### Proof

Normalize uniform weight over all wreaths so every middle resource has load one. Every lower target then has occurrence load

\[
\lambda=\frac WN=\frac{m+2}{m}.
\]

Mark each occurrence as bonus with probability

\[
p=\frac rW=\frac{2}{m+2}.
\]

The core load is

\[
\lambda(1-p)=1.
\]

Conditional on $k$ marks in one wreath, choose a uniform injection of those positions into the $r$ bonus tokens. Total fractional bonus incidence is $pW=r$, so every token has load one by symmetry.

The number $k$ must vary: $pn=2n/(m+2)$ is generally nonintegral. Bonus resources must be generic labelled tokens, not one target-specific clone per lower set.

### UNPROVED O2-G: decorated integrality

The decorated wreath hypergraph has a perfect matching for all sufficiently large $m$.

The uniformity is $2n=4m+2$. Disjoint middle pairs retain normalized wreath codegree

\[
\frac{2}{m+1}.
\tag{11.3}
\]

Thus edge size times normalized codegree does not tend to zero, and a routine fixed-uniformity nibble does not give the exact perfect matching. A specialized absorber or integral theorem remains necessary.

## 12. Adversarial audits and final ledger

### 12.1 PBBS theorem audit

The decisive Theorem 3.1 was independently rederived from the deficit-three decomposition.

- The forward step leaves $z_i$ unmatched after flipping the selected down-step.
- The reverse step is forced by the strict inequalities
  \[
  1+H_i>H_{i+1},\qquad 1+H_i>H_{i+2}-1.
  \]
- Fixed points of $\beta_S\circ\alpha_S$ are correctly bounded by the three-element reverse-unmatched set.
- The predecessor uniquely determines the center, so no factor two is missing.
- At $m=2$, the shadow theorem remains valid but the quota floor is $2$; the separate $a_1=a_3$ overload calculation is essential.
- PBBS orbit-period divisibility justifies $f(X)\ne f^{-1}(X)$.
- The stability constants $4t,2t,4t,2t$ in (4.1)-(4.4) were independently checked.
- The owner-offset phase obstruction was separately audited: $m+1$ retained step-two edges force $X_i=X_{i\pm n}$, and the trimming constants
  \[
  \delta<4B,\qquad u<8B
  \]
  and all three conditional bounds in (6.7)-(6.8) are exact.
- The component-count argument gives the exact unavoidable rebundling scale $t\ge B-b_1(P_m)$. In the orientation-preserving sewing normal form, legality is exactly (6.10), segment transition is $\theta=\pi\circ\nu$, and cycle lengths are the sums (6.12); these order conventions were checked directly.

### 12.2 Flag and matching audits

The equivariant flag construction was independently audited.

- A middle set contains at most one stabilizer-three facet.
- The quotient lower load interval is correct, including the $m=4$ endpoint.
- Both quotient matrices used are bipartite incidence matrices and hence totally unimodular.
- The pair-label result (8.9) is only a coordinate-degree statement; it is not uniformity over unordered coordinate pairs.
- The other-neighbor multiset has correct point margins but need not be bijective.
- For the desired odd $n$-cycle factor, predecessor reciprocity is the full equation (8.10), not a margin condition; arbitrary even-component $2$-factors admit an extra directed-$2$-cycle possibility.

The decorated equivalence was also audited.

- Exactly $r$, not $N$, generic bonus tokens are required.
- A variable number of marked occurrences per wreath is required.
- The converse uses one core occurrence per target and bijects all $r$ extras to tokens.
- Fractional feasibility does not imply integral matching.

### 12.3 Geodesic audit

The complementary-geodesic counts were checked by direct double counting. In particular, reversal introduces no missing factor in (7.3), and a fixed oriented segment has exactly (7.4) completions. The transfer bound separates the $d+\eta_L$ internal deficit and $2d+\eta_T$ turn deficit, giving the exact coefficient three in (7.8).

### 12.4 Proved theorem ledger

The following are unconditional:

1. the exact load identities (1.1)-(1.5);
2. the centered-edge reciprocity characterization;
3. PBBS complete first shadow with $1\le\mu\le3$;
4. $a_3\le W/(m+2)$ and $O_1(P_m)=a_3$;
5. sparse edge-change stability (4.1)-(4.4);
6. the exact lower bound $t\ge B-b_1(P_m)$ for PBBS rebundling;
7. global omitted-label balance in every spanning $2$-factor;
8. the $O(B)$-defect PBBS centered rainbow forest;
9. the owner-phase obstruction and phase-trimmed $O(B)$ skeleton;
10. the residual $f$-factor characterization;
11. the orientation-preserving legal-sewing normal form (6.9)-(6.13);
12. complementary-geodesic regularity, completion counts, codegrees, and transfer theorem;
13. the equivariant near-$\{1,2\}$ facet SDR and literal local owner flags;
14. the exact signed rank-isolated lift;
15. the optimal rainbow-core implication and residue $h\in\{0,n/3,2n/3\}$;
16. the decorated perfect-matching equivalence and its fractional solution.

### 12.5 Unproved statements

The following are sufficient routes, not proved lemmas:

- O2-A: an exact factor at PBBS edge distance $o(W)$;
- O2-B: anchored self-colored sewing of the phase-trimmed PBBS skeleton;
- O2-C: geodesic rainbow connector;
- O2-D: reciprocal flag completion with $n$-cycles;
- O2-E: positive first-shadow lift;
- O2-F: maximal rainbow reservoir inside one exact factor;
- O2-G: decorated-wreath perfect matching.

O2-A and O2-B are now the most direct. They start from a proved $O(W/m)$ PBBS shadow and ask only for exact cyclic rebundling. O2-G is the cleanest exact equivalence but asks for the stronger property of complete shadow.

### 12.6 Final implication scope

This report does not prove the requested exact factor theorem. It proves that the shadow part is already solved in the canonical PBBS $2$-factor and isolates exact reciprocity plus length-$n$ rebundling as the obstruction.

Even if any one of O2-A through O2-G is proved, the conclusion is only a depth-one unlabelled first-shadow theorem. It does not imply depth two, a fixed Gaussian window, MWB without an additional tower theorem, or labelled common-owner synchronization. Labelled synchronization remains strictly stronger.

No exact-factor conclusion is obtained by averaging across incompatible factors; every fractional relaxation is explicitly labelled. Every claimed exact-factor implication ends in one literal integral $C_n$-factor.
