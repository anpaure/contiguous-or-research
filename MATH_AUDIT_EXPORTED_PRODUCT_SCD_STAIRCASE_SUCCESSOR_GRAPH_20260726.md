# Exported product-SCD staircases: exact successor graph, weighted Hall reduction, and the parallel-fibre collision

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Outcome

Fix \(H\ge1\), and put

\[
 r=m-H-1.
\tag{0.1}
\]

For an oriented product-SCD block

\[
 u=L(D_Y)\Vert R(C_X),
 \qquad p=\mu(D),\quad a=\mu(C),
\tag{0.2}
\]

assume

\[
 p+H\le a,\qquad 2a+H\le m.
\tag{0.3}
\]

This is precisely the rank range in which the block has the \(H\)
lower states which the same-cell audit forces to leave the block.  If a
successor left chain \(E\) has first-\(t\) singleton prefix set \(P_t(E)\),
then the exact repair condition is

\[
 P_t(E)\cap\bigl(D_{a-t}\cup C_{m-a}\bigr)=\varnothing
 \qquad(1\le t\le H).
\tag{0.4}
\]

There are two sharply different cases.

* If \(E\subseteq X\), on the shore of the current right chain, then
  (0.4) collapses to the single condition

  \[
  P_H(E)\cap C_{m-a}=\varnothing.
  \tag{0.5}
  \]

  It is independent of \(D\), and also independent of the right partner
  of \(E\) in the successor block.
* If \(E\subseteq Y\), on the shore of the current left chain, then the
  full flag condition

  \[
  P_t(E)\cap D_{a-t}=\varnothing\quad(1\le t\le H)
  \tag{0.6}
  \]

  remains.

Consequently the transverse successor graph is an exact complete
blow-up of a chain-signature graph.  A right chain \(C\) has supply

\[
 s_H(C)=\binom m{\mu(C)-H},
\tag{0.7}
\]

and a possible successor left chain \(E\) has capacity \(R(E)\), the
number of admissible right partners of \(E\).  The exact block-level Hall
condition is

\[
 \boxed{
 \sum_{C\in\mathcal A}s_H(C)
 \le
 \sum_{E\in N_H(\mathcal A)}R(E)
 \quad\hbox{for every chain family }\mathcal A,}
\tag{0.8}
\]

where

\[
 C\sim_H E
 \quad\Longleftrightarrow\quad
 P_H(E)\subseteq X\setminus C_{m-\mu(C)}.
\tag{0.9}
\]

Equation (0.8) is necessary and sufficient for a transverse matching of
the product blocks.  It is the correct ordinary path-cover Hall gate.

There is, however, an exact warning.  The **uncoloured** directed graph
already has a near-perfect path cover: keep the same left chain \(D\)
from one block to the next.  At most one outgoing staircase per \(D\)
fibre is lost.  For \(H=O(\sqrt m)\), the total loss is \(o(W_m)\).
Nevertheless this path cover is physically useless.  For every fixed
right chain \(C\), all its parallel repairs have the same \(X\)-section
\(C_{m-a}\), and hence

\[
 H\,N_{\parallel}(C)\le\binom ma.
\tag{0.10}
\]

Since there are exactly \(\binom m{a-H}\) source blocks with right chain
\(C\), at \(a=m/2-x\sqrt m+O(1)\) and
\(H=A\sqrt m+O(1)\),

\[
 \frac{N_{\parallel}(C)}{\binom m{a-H}}
 \le
 \frac{e^{4Ax+2A^2+o(1)}}{H}=o(1).
\tag{0.11}
\]

Uniformly on any fixed admissible Gaussian \(x\)-window, the parallel
path cover therefore has a \(\Theta_A(W_m)\) middle-target collision.
Almost every repaired Gaussian staircase is forced to be transverse.
Those transverse arcs alternate the two physical shores.

Thus neither a positive-degree argument nor an ordinary near-perfect
path cover closes the mixed-word gate.  What survives is (0.8), together
with capacity one for every produced middle target and a sublinear
component/seam condition.  These last two requirements are written
exactly in Section 8.

## 1. Chain and prefix notation

Fix SCDs \(\mathcal C_X,\mathcal C_Y\) of two disjoint \(m\)-cubes.  For a
chain \(E\), let \(\mu(E)=e\) be its minimum rank and write

\[
 E_e\subset E_{e+1}\subset\cdots\subset E_{m-e},
 \qquad E_j\setminus E_{j-1}=\{\epsilon_j\}.
\tag{1.1}
\]

Its active length is

\[
 \lambda(E)=m-2e.
\tag{1.2}
\]

When \(\lambda(E)\ge H\), the first \(t\) letters of \(L(E)\) are
singletons.  Their union is

\[
 P_t(E)=
 \{\epsilon_{m-e-t+1},\ldots,\epsilon_{m-e}\},
 \qquad1\le t\le H.
\tag{1.3}
\]

In particular

\[
 P_1(E)\subset\cdots\subset P_H(E),
 \qquad |P_t(E)|=t.
\tag{1.4}
\]

We call \(P_H(E)\) the \(H\)-prefix signature of \(E\).  A chain with
\(\lambda(E)<H\) cannot supply an \(H\)-step singleton staircase and is
not a successor vertex for the present exact graph.

## 2. Exact exported staircase

### Lemma 2.1 (the \(H\) outgoing states)

Under (0.2)--(0.3), define, for \(1\le t\le H\),

\[
 T_t=D_{a-t}\cup C_{m-a-H+t}.
\tag{2.1}
\]

Then \(T_t\) is a rank-\((m-H)\) target with a canonical witness starting
in \(L(D)\) and ending in \(R(C)\).  If the same start is continued to the
end of the current block, its union is

\[
 B_t=D_{a-t}\cup C_{m-a},
 \qquad |B_t|=m-t.
\tag{2.2}
\]

If a successor begins with the singleton prefix (1.3), then the interval
from this start through its \(t\)-th successor letter is a rank-\(m\)
interval if and only if

\[
 P_t(E)\cap B_t=\varnothing.
\tag{2.3}
\]

In that event its middle target is exactly

\[
 M_t(u,E)=B_t\cup P_t(E).
\tag{2.4}
\]

#### Proof

The inequalities in (0.3) give

\[
 p\le a-H\le a-t\le m-p
\]

and

\[
 a\le m-a-H+t\le m-a.
\]

Thus both chain members in (2.1) exist.  Their shores are disjoint and
their ranks add to (m-H).  The canonical suffix-prefix witness is the
standard product-SCD witness.  Continuing to the end of \(R(C)\) replaces
the second component by \(C_{m-a}\), proving (2.2).  Finally \(P_t(E)\)
has \(t\) distinct coordinates.  Since \(|B_t|=m-t\), the union in (2.4)
has rank \(m\) exactly when the two sets are disjoint.  This proves
(2.3). \(\square\)

### Corollary 2.2 (shore reduction)

If \(E\subseteq X\), then (2.3) for every \(t\) is equivalent to (0.5).
If \(E\subseteq Y\), it is equivalent to (0.6).

#### Proof

In the first case \(P_t(E)\) is automatically disjoint from
\(D_{a-t}\subseteq Y\).  Since the \(P_t(E)\) are nested, disjointness
from the fixed set \(C_{m-a}\) for every \(t\) is equivalent to
disjointness for \(t=H\).  The other case is the same disjoint-shore
argument with the roles reversed. \(\square\)

The transverse outputs in (2.4) are internally distinct: their
\(X\)-ranks are \(m-a+t\).  Parallel outputs need not be internally
distinct; equality can occur when a newly read \(E\)-label is exactly
the \(D\)-increment removed between \(D_{a-t}\) and \(D_{a-t-1}\).

## 3. The oriented successor vertices and their capacities

Orient every product cell with the smaller-minimum chain on the left.
For equal minima, use the (X)-chain on the left.  This fixes every cell
exactly once and is the orientation which avoids the audited terminal
upper-endpoint defect.

For a left chain \(E\subseteq S\), let \(R_S(E)\) be the number of cells
whose oriented left chain is \(E\).  Put

\[
 u(e)=\min\{\lfloor m/2\rfloor,r-e\}.
\tag{3.1}
\]

Telescoping the SCD chain counts

\[
 A_m(f)=\binom mf-\binom m{f-1}
\tag{3.2}
\]

gives the exact capacities

\[
 \begin{aligned}
 R_X(E)&=
 \begin{cases}
 \binom m{u(e)}-\binom m{e-1},&e\le u(e),\\
 0,&e>u(e),
 \end{cases}\\
 R_Y(E)&=
 \begin{cases}
 \binom m{u(e)}-\binom me,&e<u(e),\\
 0,&e\ge u(e).
 \end{cases}
 \end{aligned}
\tag{3.3}
\]

The difference is only the fixed tie convention.  Any other tie
orientation changes only the corresponding \(A_m(e)\) term.

For the source block (0.2), define the shore-dependent forbidden flag

\[
 F_t^X(u)=C_{m-a},
 \qquad
 F_t^Y(u)=D_{a-t}.
\tag{3.4}
\]

There is an arc from \(u\) to a distinct successor cell with left chain
\(E\subseteq S\) precisely when

\[
 \lambda(E)\ge H,
 \qquad
 P_t(E)\cap F_t^S(u)=\varnothing
 \quad(1\le t\le H).
\tag{3.5}
\]

The right partner of (E) does not occur in (3.5).  Thus every admissible
chain \(E\) contributes exactly \(R_S(E)\) successor cells, except that
one subtracts the current cell if it would be a parallel self-successor.

## 4. Exact degrees and codegrees

Ignoring only the explicitly excluded self-cell, the outdegree of (u)
is

\[
 d^+(u)=
 \sum_{S\in\{X,Y\}}
 \sum_{\substack{E\in\mathcal C_S:\lambda(E)\ge H\\
 P_t(E)\cap F_t^S(u)=\varnothing\ (1\le t\le H)}}
 R_S(E).
\tag{4.1}
\]

For sources (u_1,\ldots,u_j), their common successor count is

\[
 \sum_{S\in\{X,Y\}}
 \sum_{\substack{E\in\mathcal C_S:\lambda(E)\ge H\\
 P_t(E)\cap\bigcup_{i=1}^jF_t^S(u_i)=\varnothing\ (1\le t\le H)}}
 R_S(E),
\tag{4.2}
\]

again with the finitely many forbidden self-cells removed.  This is the
exact all-order codegree formula.

In particular, for two sources with right chains (C,C'\subseteq X),
their transverse codegree is

\[
 \boxed{
 \sum_{\substack{E\in\mathcal C_X:\lambda(E)\ge H\\
 P_H(E)\cap(C^+\cup C'^+)=\varnothing}}
 R_X(E),}
\tag{4.3}
\]

where (C^+=C_{m-\mu(C)}).  Sources having the same right chain have
identical transverse neighborhoods.  Formula (4.3), rather than an
owner-codegree estimate, is the exact prefix-signature statistic which a
positive theorem has to control.

## 5. Collapse to the weighted transverse Hall condition

Fix a right chain (C\subseteq X) of minimum (a) satisfying

\[
 2a+H\le m.
\tag{5.1}
\]

Every chain \(D\subseteq Y\) with \(\mu(D)\le a-H\) gives a source block
\(L(D)\Vert R(C)\).  Its tail condition is automatic, because

\[
 \mu(D)+a\le2a-H\le m-2H\le m-H-1=r.
\tag{5.2}
\]

Therefore the number of source clones of (C) is exactly

\[
 s_H(C)=\sum_{p=0}^{a-H}A_m(p)=\binom m{a-H}.
\tag{5.3}
\]

Define the chain-signature graph (Gamma_H^X) by

\[
 C\sim E
 \quad\Longleftrightarrow\quad
 \lambda(E)\ge H
 \quad\hbox{and}\quad
 P_H(E)\cap C^+=\varnothing.
\tag{5.4}
\]

Replace \(C\) by \(s_H(C)\) left clones and \(E\) by \(R_X(E)\) right
clones.  By Corollary 2.2, the transverse cell graph is exactly this
complete blow-up.

### Theorem 5.1 (exact transverse Hall reduction)

There is a transverse matching of every source block to a distinct
successor block if and only if, for every family \(\mathcal A\) of right
chains,

\[
 \sum_{C\in\mathcal A}s_H(C)
 \le
 \sum_{E\in N_{\Gamma_H^X}(\mathcal A)}R_X(E).
\tag{5.5}
\]

More generally, the exact number of unmatched source blocks is

\[
 \boxed{
 \Delta_H^X=
 \max_{\mathcal A}
 \left(
 \sum_{C\in\mathcal A}s_H(C)-
 \sum_{E\in N_{\Gamma_H^X}(\mathcal A)}R_X(E)
 \right)_+.}
\tag{5.6}
\]

The same statement holds with (X,Y) interchanged.

#### Proof

This is Hall's theorem applied to the clone graph.  The standard
deficiency form of Hall gives (5.6).  All clones of one chain have the
same neighborhood, so maximizing over arbitrary clone families is
equivalent to taking all clones of each chain in a chain family
\(\mathcal A\). \(\square\)

The two shore matchings use disjoint successor orientations.  A
transverse arc sends a (Y)-left block to an (X)-left block, or vice
versa.  Hence selected transverse arcs automatically alternate shores,
and every directed transverse cycle has even length.

The weighted indegree of a successor type (E) is also exact:

\[
 d^-_{\rm wt}(E)=
 \sum_{\substack{C:\ 2\mu(C)+H\le m\\
 P_H(E)\cap C^+=\varnothing}}
 s_H(C).
\tag{5.7}
\]

## 6. An uncoloured near-perfect path cover exists

The parallel graph contains a canonical family of arcs.  Fix a left
chain (D), and list in any order all source blocks

\[
 L(D)\Vert R(C_1),\ldots,L(D)\Vert R(C_ell).
\tag{6.1}
\]

Use the next copy of \(L(D)\) as the prefix following each block.  For a
source with right minimum \(a\), the first-\(t\) set \(P_t(D)\) consists
of the top (t) increments of (D).  Since the tail condition gives
(a\le m-p),

\[
 P_t(D)\cap D_{a-t}=\varnothing
 \qquad(1\le t\le H).
\tag{6.2}
\]

Thus every consecutive pair in (6.1) is a legal successor arc.  Closing
the list cyclically gives a directed cycle when (ell\ge2); opening it
gives a path and loses only the final outgoing staircase.

There are exactly

\[
 \binom m{\lfloor m/2\rfloor}
\tag{6.3}
\]

chains in an SCD of (Q_m).  Hence all such fibres can be opened at a
cost of at most

\[
 H\binom m{\lfloor m/2\rfloor}=o\!\left(\binom{2m}m\right)
\tag{6.4}
\]

when \(H=O(\sqrt m)\).  Equation (6.4) follows from the central binomial
asymptotics: its left side is \(O(2^m)\), while
\(\binom{2m}m=\Theta(4^m/\sqrt m)\).

Thus the ordinary directed graph has an uncoloured near-perfect path
cover.  The next section proves that this does not give a common middle
baseline.

## 7. Exact parallel target-capacity obstruction

Fix a right chain (C\subseteq X) of minimum (a).  For every parallel
repair, the successor prefix lies in (Y).  Therefore every middle set
in (2.4) has

\[
 M_t\cap X=C_{m-a},
 \qquad |M_t\cap Y|=a.
\tag{7.1}
\]

There are only \(\binom ma\) possible sets with the fixed \(X\)-section
in (7.1).  Distinct middle witnesses ending at distinct baseline
positions must have distinct target names.  Consequently, if
\(N_{\parallel}(C)\) source blocks with right chain \(C\) are completely
repaired in parallel, then

\[
 \boxed{H N_{\parallel}(C)\le\binom ma.}
\tag{7.2}
\]

This bound grants every possible rank-(a) (Y)-section, whether or not
it is generated by the chosen SCD prefixes.  It is therefore stronger
than any prefix-specific obstruction.

There are (s_H(C)=\binom m{a-H}) source blocks in this fibre.  If

\[
 a=\frac m2-x\sqrt m+O(1),
 \qquad H=A\sqrt m+O(1),
\tag{7.3}
\]

with fixed \(A>0\) and \(x\) in a compact subset of \((A/2,\infty)\), then

\[
 \frac{\binom m{a-H}}{\binom ma}
 =\prod_{j=0}^{H-1}\frac{a-j}{m-a+j+1}
 =\exp(-4Ax-2A^2+o(1)),
\tag{7.4}
\]

uniformly on that compact set.  Indeed, Taylor expansion of the logarithm
has total quadratic error \(O(H/m)=o(1)\), while its linear term is

\[
 -\frac4m\sum_{j=0}^{H-1}(x\sqrt m+j)+o(1)
 =-4Ax-2A^2+o(1).
\tag{7.5}
\]

Combining (7.2)--(7.4) gives (0.11).  Thus only \(o(1)\) of the source
blocks in every such fixed-(C) Gaussian fibre can be repaired in
parallel.

For exact global accounting, let \(I\subset(A/2,\infty)\) be a fixed
nonempty compact interval and sum over

\[
 \frac{m/2-a}{\sqrt m}\in I.
\tag{7.6}
\]

The standard uniform local limits give

\[
 \sum_{a\text{ in }(7.6)}
 H A_m(a)\binom m{a-H}
 =\Theta_{A,I}\!\left(\binom{2m}m\right),
\tag{7.7}
\]

whereas the total number of different middle targets allowed by (7.1)
is at most

\[
 \sum_{a\text{ in }(7.6)}A_m(a)\binom ma
 =O_{A,I}\!\left(\frac1{\sqrt m}\binom{2m}m\right).
\tag{7.8}
\]

To verify the scales, uniformly in (7.6),

\[
 A_m(a)=\Theta_{A,I}(2^m/m),
 \quad
 \binom m{a-H}=\Theta_{A,I}(2^m/\sqrt m),
 \quad
 H=\Theta_A(\sqrt m),
\tag{7.9}
\]

and there are \(\Theta(\sqrt m)\) possible \(a\)'s.  Equations
(7.7)--(7.8) follow using
\(\binom{2m}m=\Theta(4^m/\sqrt m)\).

Therefore the fibrewise path cover from Section 6 has a
\(\Theta_{A,I}(W_m)\) floor-corrected middle-target collision.  Any
successful repair routes all but \(o(1)\) of these Gaussian source blocks
transversely.

## 8. The exact surviving integral system

For a legal arc \(e=(u,v)\), let

\[
 \Phi(e)=\{M_t(u,E_v):1\le t\le H\}
\tag{8.1}
\]

be its produced middle-target bundle.  Parallel arcs with
(|\Phi(e)|<H) are already defective.  A literal common-baseline
selection requires binary variables (x_e) satisfying

\[
 \begin{aligned}
 &\sum_{e\text{ out of }u}x_e\le1,\\
 &\sum_{e\text{ into }v}x_e\le1,\\
 &\sum_{e:\ M\in\Phi(e)}x_e\le1
 &&\text{for every rank-}m\text{ target }M,\\
 &x_e\in\{0,1\}.
 \end{aligned}
\tag{8.2}
\]

Near-perfect repair means

\[
 \sum_e |\Phi(e)|x_e
 \ge H|\mathscr U|-o(W_m),
\tag{8.3}
\]

where (mathscr U) is the compulsory source-block family under study.

The weighted Hall condition (5.5) is exactly the projection of (8.2) to
the first two lines.  It is not sufficient for the third line, as the
parallel-fibre construction proves.  A further necessary target Hall
inequality is

\[
 H|\mathcal A|
 \le
 \left|\bigcup_{u\in\mathcal A}
              \bigcup_{e\text{ out of }u}\Phi(e)\right|
 +o(W_m)
\tag{8.4}
\]

for every source family \(\mathcal A\), but (8.4) alone is not sufficient
because the (H) target choices belonging to one arc are bundled.

Finally, a matching in (8.2) forms vertex-disjoint directed paths and
cycles.  A transverse cycle has even length.  Turning every cycle into a
literal linear path deletes one arc, hence loses at most (H) repaired
states per cycle.  Thus a coefficient-one implementation also needs

\[
 \#\{\text{selected directed cycles}\}=o(W_m/H)
\tag{8.5}
\]

or an additional legal cycle-splicing operation.

## 9. Precise boundary

The following are proved.

1. Equations (0.4)--(0.6) are the exact chronology-sensitive successor
   conditions for the exported lower staircase.
2. Equations (4.1)--(4.3) give the exact degrees and all codegrees.
3. The transverse graph is the weighted chain-signature blow-up, and
   (5.5) is its necessary-and-sufficient block-level Hall theorem.
4. The uncoloured graph has an explicit near-perfect parallel path cover.
5. That cover, and in fact every predominantly parallel routing, has a
   \(\Theta_A(W_m)\) middle-target collision on a fixed Gaussian window.
   Hence almost every successful Gaussian repair must be transverse.

What is not proved is the weighted Hall inequality (5.5) for an arbitrary
fixed SCD, nor the target-bundle and component conditions (8.2)--(8.5).
The exact remaining constructive statement is therefore:

> Find a transverse, shore-alternating selection in the chain-signature
> graph (5.4) which satisfies weighted Hall (5.5), has disjoint target
> bundles in (8.2), and has \(o(W_m/H)\) path/cycle seams.

No coefficient-one conclusion is claimed.
