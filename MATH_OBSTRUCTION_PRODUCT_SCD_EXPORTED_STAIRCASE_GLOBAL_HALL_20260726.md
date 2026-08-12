# Exported product-SCD staircases have a global target-name Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Result

Put

\[
 W_m={2m\choose m},\qquad H=\lceil A\sqrt m\rceil,
 \qquad Q=H+1,
 \tag{0.1}
\]

where \(A>0\) is fixed.  Consider the exact product-SCD tail at cutoff
\(r=m-Q\).  The surviving local escape in the endpoint audit orients an
imbalanced chain pair as

\[
             L(D)\Vert R(C)                         \tag{0.2}
\]

and exports its \(Q\) lower starts into a singleton prefix of a successor
block.  Section 2 below defines the resulting directed, target-labelled
block graph exactly.

The ordinary directed graph can have large degrees.  Nevertheless its
capacity-one target lift has a linear Hall cut.  There is a family
\(\mathscr A_m\) of actual exported lower states such that, even after

* allowing every state to choose an arbitrary successor block;
* ignoring all successor-block and owner capacities;
* allowing the successor prefix to lie in either half-cube; and
* allowing the states of one packet to choose the two shores
  independently,

one has

\[
 \boxed{
 |\mathscr A_m|-|N(\mathscr A_m)|\ge c_AW_m-o(W_m)
 }
 \tag{0.3}
\]

for a constant \(c_A>0\).  The relaxation in the third and fourth bullets
is stronger than an actual path cover, in which one successor block has
only one first shore and one ordered prefix.

The obstruction is an exact target-name collision.  Fix a half-chain
\(D\) and a rank \(j\).  All exported states with right-chain minimum

\[
                  j+1\le a\le j+Q                 \tag{0.4}
\]

have the same half projection \(D_j\) after an opposite-half completion.
Their number is

\[
 \sum_{a=j+1}^{j+Q}
 \left({m\choose a}-{m\choose {a-1}}\right)
 ={m\choose {j+Q}}-{m\choose j},                    \tag{0.5}
\]

whereas that target fibre contains only \({m\choose j}\) middle sets.
At Gaussian ranks,

\[
 { {m\choose {j+Q}}\over {m\choose j}}
 \longrightarrow e^{4Ay-2A^2},
 \qquad j={m\over2}-y\sqrt m+O(1).                 \tag{0.6}
\]

Choose a fixed interval of \(y\)'s on which the last limit is greater
than \(3\).  Summing (0.5) over \(\Theta(\sqrt m)\) values of \(j\), and
then over \(\Theta_A(2^m/\sqrt m)\) eligible chains \(D\), gives (0.3).
The same-half completion escape has only \(O_A(W_m/\sqrt m)\) target
names and cannot repair the cut.

The constant \(3\), rather than \(2\), makes the same cut survive the
grant of one optional distinguished odd-lift coordinate.  Thus the first
copy of the trimmed odd lift still has a positive-density cut after
normalization by \({2m+1\choose m}\sim2W_m\).

Consequently no near-perfect path cover of intact product-SCD blocks can
realize the exported-staircase baseline coupling, even if its unlabelled
block adjacency is perfect.  A surviving mixed construction must abandon
a positive density of these canonical exported states, split/interlace
the chain blocks so that a completion prefix uses both half-cubes, or
replace the product-SCD carrier.  This is not a lower bound for arbitrary
contiguous-OR words and is not a coefficient-one conclusion.

## 1. Exact source packets

Fix SCDs of two disjoint \(m\)-cubes \(X\) and \(Y\).  A chain of
minimum rank \(a\) is written

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}.
 \tag{1.1}
\]

The number of such chains in any SCD is

\[
 A_m(a)={m\choose a}-{m\choose {a-1}}.              \tag{1.2}
\]

Let \(D\) be a chain in \(Y\), of minimum rank \(b\), and let \(C\)
be a chain in \(X\), of minimum rank \(a\).  Assume

\[
 a-Q\ge b,\qquad 2a+Q-1\le m,
 \qquad a+b\le m-Q.                                 \tag{1.3}
\]

Then the oriented tail block \(u=(D,C)\) is

\[
                      L(D)\Vert R(C).               \tag{1.4}
\]

For \(0\le k<Q\), its canonical exported lower target is

\[
 T_{u,k}=D_{a-Q+k}\cup C_{m-a-k}.                   \tag{1.5}
\]

All displayed chain members exist by (1.3), and

\[
                         |T_{u,k}|=m-Q.              \tag{1.6}
\]

After the whole block has been read from the start of (1.5), the current
union is

\[
 B_{u,k}=D_{a-Q+k}\cup C_{m-a},
 \qquad |B_{u,k}|=m-Q+k.                            \tag{1.7}
\]

Thus exactly \(Q-k\) new coordinates are needed to reach rank \(m\).

It is useful to replace \(k\) by

\[
 j=a-Q+k,qquad t=Q-k=a-j.                          \tag{1.8}
\]

Then \(1\le t\le Q\), and

\[
 T_{u,k}=D_j\cup C_{m-Q-j},
 \qquad B_{u,k}=D_j\cup C_{m-a}.                   \tag{1.9}
\]

For fixed \(D,j\), the lower targets in (1.9), as \(C\) ranges over
chains whose minimum satisfies (0.4), are distinct.  Indeed all their
\(X\)-projections have the same rank \(m-Q-j\), and an SCD partitions
that rank into distinct chain members.  Targets belonging to different
\((D,j)\)'s are also distinct: their \(Y\)-projections are distinct or
have different sizes.

## 2. The directed exported-staircase graph

Let \(\mathfrak D_Q\) be the following directed, bundle-labelled graph.
Its vertices are oriented tail blocks.  A source \(u=(D,C)\) satisfying
(1.3) may point to a successor block \(v\) when the first \(Q\) entries
of \(v\) are singleton letters \(z_1,\ldots,z_Q\) and every prefix
needed in (1.7) is disjoint from the current union.

There are two possible shores.

* If the prefix lies in \(X\), then it is enough and necessary for the
  full packet that

  \[
       \{z_1,\ldots,z_Q\}\cap C_{m-a}=\varnothing.
       \tag{2.1}
  \]

  The target carried by state \(k\), with \(j,t\) as in (1.8), is

  \[
       M^X_{u,v,k}
       =D_j\cup C_{m-a}\cup\{z_1,\ldots,z_t\}.       \tag{2.2}
  \]

  Its \(Y\)-projection is exactly \(D_j\), and its \(X\)-projection has
  rank \(m-j\).

* If the prefix lies in \(Y\), then the corresponding condition is

  \[
       \{z_1,\ldots,z_{Q-k}\}\cap D_{a-Q+k}
       =\varnothing
       \qquad(0\le k<Q),
       \tag{2.3}
  \]

  for the respective state \(k\).  Equivalently, with \(j,t\) from
  (1.8), the exact triangular condition is

  \[
       \{z_1,\ldots,z_t\}\cap D_j=\varnothing.
       \tag{2.3a}
  \]

  The stronger full-prefix condition
  \(\{z_1,\ldots,z_Q\}\cap D_{a-1}=\varnothing\) is sufficient for the
  whole packet but is not necessary.  We do not impose it in the Hall
  cut below.

  Whenever (2.3a) holds, the carried target is

  \[
       M^Y_{u,v,k}
       =D_j\cup C_{m-a}\cup\{z_1,\ldots,z_t\}.       \tag{2.4}
  \]

  Its \(X\)-projection is exactly \(C_{m-a}\), and its \(Y\)-projection
  has rank \(a\).

Every target in (2.2) or (2.4) has rank \(m\).  An integral block path
cover selects directed edges with indegree and outdegree at most one.
The coefficient-one endpoint coupling additionally requires the carried
middle target names to have capacity one.  Accordingly define the
target lift \(\mathfrak H_Q\): its left vertices are source-state clones
\((u,k)\), its right vertices are rank-\(m\) target names, and adjacency
means that some directed edge of \(\mathfrak D_Q\) carries that name.

For the Hall argument, enlarge this graph once more.  Permit the
completion of each source state to end at an arbitrary position before
the successor leaves its first half-cube, even if that one-shore prefix
contains overlaps or a nonsingleton chain core.  If the first shore is
\(X\), every rank-\(m\) completion still has \(Y\)-projection exactly
\(D_j\).  If it is \(Y\), every such completion still has
\(X\)-projection exactly \(C_{m-a}\).  Thus Lemmas 3.1--3.2 apply
unchanged to this larger one-shore target graph.  The proof below does
not rely on singleton increments or on (2.1)/(2.3); those conditions
only describe the original explicit \(Q\)-prefix edges.

Any path-cover coupling gives a matching in \(\mathfrak H_Q\).  The
converse need not hold, since \(\mathfrak H_Q\) forgets successor and
owner capacities and lets clones of one packet choose different
successor shores.  Thus a Hall cut in \(\mathfrak H_Q\) is also a Hall
cut for every integral path cover.

To spell out the capacity-one point, the \(Q\) clones of one selected
edge end at its \(Q\) distinct successor-prefix positions.  The
indegree-one condition makes these positions distinct across different
sources.  On the other hand, chosen witnesses for distinct members of
the rank-\(m\) antichain have distinct right endpoints.  Moreover the
target name at one completion endpoint is forced: every interval ending
there is nested with the exported completion interval, so any other
rank-\(m\) union ending there must equal the same rank-\(m\) set.  Hence,
in a word of length \(W_m+o(W_m)\), all but \(o(W_m)\) of these physical
positions must be credited to distinct rank-\(m\) target names.  A Hall
deficiency of order \(W_m\) cannot be hidden among the excess positions.

## 3. The exact fibre cut

Choose fixed compact intervals

\[
 I=[Y_0,Y_1],\qquad K=[Z_0,Z_1]                     \tag{3.1}
\]

of positive lengths such that

\[
 \begin{split}
 &Y_0>{3A\over2},\\
 &\rho:=e^{4AY_0-2A^2}>3,\\
 &Z_0>Y_1+A.
 \end{split}                                       \tag{3.2}
\]

Such intervals exist for every fixed \(A>0\).  Shrinking their lengths
if necessary preserves all three strict inequalities.

Let

\[
 \begin{split}
 J_m&=\left\{j:\ {m/2-j\over\sqrt m}\in I\right\},\\
 \mathcal D_m&=\left\{D:\ {m/2-\min(D)\over\sqrt m}\in K\right\}.
 \end{split}                                       \tag{3.3}
\]

Integer endpoints in (3.3) may be rounded arbitrarily.  The strict
margins in (3.2) absorb every \(O(1)\) floor error.

For each \(D\in\mathcal D_m\), \(j\in J_m\), and every \(X\)-chain
\(C\) whose minimum \(a\) lies in

\[
                         j+1\le a\le j+Q,           \tag{3.4}
\]

put the source clone \((u,k)\), where

\[
 u=(D,C),\qquad k=Q-a+j,                            \tag{3.5}
\]

into \(\mathscr A_m\).  Equations (3.2) imply (1.3) uniformly for all
these choices when \(m\) is sufficiently large:

* \(Z_0>Y_1+A\) gives \(b\le a-Q\);
* \(Y_0>3A/2\) gives \(2a+Q-1\le m\); and
* the same inequalities give \(a+b\le m-Q\).

The exact number of clones is

\[
 \begin{split}
 |\mathscr A_m|
 &=|\mathcal D_m|
   \sum_{j\in J_m}\sum_{a=j+1}^{j+Q}A_m(a)\\
 &=|\mathcal D_m|
   \sum_{j\in J_m}
   \left({m\choose {j+Q}}-{m\choose j}\right).
 \end{split}                                       \tag{3.6}
\]

The second line is the exact telescoping identity (0.5).

### Lemma 3.1 (opposite-shore target capacity)

The union of all neighbors of \(\mathscr A_m\) obtained from prefixes in
\(X\) has size at most

\[
             |\mathcal D_m|\sum_{j\in J_m}{m\choose j}.
 \tag{3.7}
\]

#### Proof

By (2.2), a neighbor of a clone indexed by \((D,j)\) has \(Y\)-projection
exactly \(D_j\).  The number of rank-\(m\) sets with this projection is

\[
                {m\choose {m-j}}={m\choose j}.       \tag{3.8}
\]

The fibres are disjoint.  Members of one SCD at rank \(j\) are distinct,
and fibres belonging to different \(j\)'s have different projection
sizes.  Summing (3.8) proves (3.7). \(\square\)

### Lemma 3.2 (same-shore escape is sublinear)

Let

\[
 I_m^*=\bigcup_{j\in J_m}[j+1,j+Q].                 \tag{3.9}
\]

The union of all neighbors obtained from prefixes in \(Y\) has size at
most

\[
                   \sum_{a\in I_m^*}A_m(a){m\choose a}
                   =O_A(4^m/m).                     \tag{3.10}
\]

#### Proof

By (2.4), such a target has \(X\)-projection equal to the maximum
\(C_{m-a}\) of its source chain.  For fixed \(C\), there are at most
\({m\choose a}\) possible \(Y\)-projections of rank \(a\).  Distinct
chains have distinct maxima, so summing this deliberately generous bound
gives the left side of (3.10).

All ranks in \(I_m^*\) lie in a fixed Gaussian window.  Uniformly there,

\[
 A_m(a)=O_A(2^m/m),\qquad {m\choose a}=O_A(2^m/\sqrt m),
 \tag{3.11}
\]

and \(|I_m^*|=O_A(\sqrt m)\).  This proves (3.10). \(\square\)

The two capacity lemmas use only the shore which remains untouched.  In
Lemma 3.1 every completion confined to \(X\), with arbitrary internal
letters and order, retains the \(Y\)-projection \(D_j\).  In Lemma 3.2
every completion confined to \(Y\) retains the \(X\)-projection
\(C_{m-a}\).  Therefore (3.7) and (3.10) remain valid after granting an
arbitrary one-shore completion word; singleton prefixes and the exact
legality conditions (2.1), (2.3a) only restrict these already bounded
target universes further.

Combining the two lemmas with (3.6) gives the exact finite-\(m\) cut

\[
 \begin{split}
 |\mathscr A_m|-|N(\mathscr A_m)|
 \ \ge{}& |\mathcal D_m|
   \sum_{j\in J_m}
   \left({m\choose {j+Q}}-2{m\choose j}\right)\\
 &-\sum_{a\in I_m^*}A_m(a){m\choose a}.
 \end{split}                                       \tag{3.12}
\]

This inequality already ignores every block-level collision and is
therefore valid under arbitrary ordering and arbitrary path-cover choices.

## 4. Gaussian accounting

Uniformly for \(j=m/2-y\sqrt m+O(1)\), \(y\in I\), the local central
limit estimate gives

\[
 {m\choose j}
 =\left(\sqrt{2/\pi}\,e^{-2y^2}+o(1)\right)
   {2^m\over\sqrt m},                               \tag{4.1}
\]

and, since \(Q=A\sqrt m+O(1)\),

\[
 { {m\choose {j+Q}}\over {m\choose j}}
 =e^{4Ay-2A^2}+o(1)\ge\rho-o(1).                   \tag{4.2}
\]

Also, uniformly for \(b=m/2-z\sqrt m+O(1)\), \(z\in K\),

\[
 A_m(b)=
 \left(4z\sqrt{2/\pi}\,e^{-2z^2}+o(1)\right)
 {2^m\over m}.                                     \tag{4.3}
\]

Consequently

\[
 \begin{split}
 |\mathcal D_m|
 &=\left(c_K+o(1)\right){2^m\over\sqrt m},\\
 \sum_{j\in J_m}{m\choose j}
 &=\left(c_I+o(1)\right)2^m,
 \end{split}                                       \tag{4.4}
\]

where

\[
 \begin{split}
 c_K&=\int_K4z\sqrt{2/\pi}\,e^{-2z^2}\,dz>0,\\
 c_I&=\int_I\sqrt{2/\pi}\,e^{-2y^2}\,dy>0.
 \end{split}                                       \tag{4.5}
\]

Insert (4.2)--(4.4) and Lemma 3.2 into (3.12).  Since

\[
 W_m=\left({1\over\sqrt\pi}+o(1)\right){4^m\over\sqrt m},
 \tag{4.6}
\]

we obtain

\[
 \begin{split}
 |\mathscr A_m|-|N(\mathscr A_m)|
 &\ge
 \left((\rho-2)c_Kc_I+o_A(1)\right){4^m\over\sqrt m}
 -O_A(4^m/m)\\
 &\ge c_AW_m
 \end{split}                                       \tag{4.7}
\]

for all sufficiently large \(m\), with for example any fixed

\[
 0<c_A<{\sqrt\pi\over2}(\rho-2)c_Kc_I.             \tag{4.8}
\]

This proves (0.3).

### Corollary 4.1 (no near-perfect labelled path cover)

For every selection of directed block edges with indegree and outdegree
at most one, at least

\[
                         c_AW_m-o(W_m)              \tag{4.9}
\]

members of \(\mathscr A_m\) fail to receive distinct middle target
names from their exported-prefix completions.  This remains true if the
unlabelled selected edges cover every block.

Since one intact source block contributes only
\(Q=\Theta_A(\sqrt m)\) clones, every repair which works by discarding
or re-witnessing whole source blocks must alter at least

\[
             \Omega_A(W_m/Q)=\Omega_A(W_m/\sqrt m)
             \tag{4.10}
\]

blocks.

#### Proof

Every such assignment is a matching in the relaxation
\(\mathfrak H_Q\).  By Hall's theorem, at most
\(|\mathscr A_m|-(c_AW_m-o(W_m))\) members of the deficient family can
be matched.  A source block contains at most \(Q\) members of
\(\mathscr A_m\), so covering the deficiency by whole-block alterations
requires at least the quotient in (4.10).  The conclusion follows.
\(\square\)

## 5. One distinguished odd-lift coordinate does not repair the cut

Grant a new coordinate \(z_*\) and allow every middle target either to
avoid or contain it.  For a fixed \((D,j)\) fibre, the opposite-shore
target capacity is now at most

\[
                         {m\choose j}+{m\choose {j+1}}.
 \tag{5.1}
\]

Indeed the \(X\)-projection has rank \(m-j\) without \(z_*\), and rank
\(m-1-j\) with \(z_*\).  The same-shore bound becomes

\[
 \sum_{a\in I_m^*}A_m(a)
 \left({m\choose a}+{m\choose {a-1}}\right)
 =O_A(4^m/m).                                      \tag{5.2}
\]

Therefore the analogue of (3.12) is

\[
 \begin{split}
 |\mathscr A_m|-|N_*(\mathscr A_m)|
 \ \ge{}& |\mathcal D_m|\sum_{j\in J_m}
 \left({m\choose {j+Q}}-2{m\choose j}
                   -{m\choose {j+1}}\right)\\
 &-O_A(4^m/m).                                     \tag{5.3}
\end{split}

Uniformly on \(J_m\),

\[
              {{m\choose {j+1}}\over {m\choose j}}=1+o(1).
 \tag{5.4}
\]

The choice \(\rho>3\) in (3.2) therefore makes (5.3) at least
\(c_A'W_m\) for some \(c_A'>0\).  Since
\({2m+1\choose m}\sim2W_m\), this is still a positive normalized Hall
deficit in the standard odd lift.

## 6. Precise boundary

The proved statement is stronger than a failure of a particular block
ordering.  It grants arbitrary outgoing degrees and discards the
indegree-one, owner-disjointness, and common-successor constraints of a
path cover.  The failure occurs only after the middle target names are
given their necessary unit capacities.

The theorem closes the following architecture:

1. retain the exact oriented product-SCD blocks;
2. retain their canonical \(Q\)-state lower export packets;
3. complete every packet before leaving the first half-cube of one
   successor product block; and
4. use those completions as the shared middle baseline.

It does not close a construction which re-witnesses a positive density of
the lower targets, splits a chain word among several distant positions,
or interlaces a completion prefix using coordinates from both half-cubes.
Those operations leave the directed exported-staircase graph defined in
Section 2.  Thus the exact remaining mixed PBBS/product-SCD statement is a
two-shore interlaced rethreading theorem: a surviving completion must
cross the successor's internal shore boundary (or otherwise alter the
canonical exported state), not merely replace its singleton prefix by a
more general word on the same shore.  It is not an ordinary path-cover
theorem on intact product cells.

No coefficient-one theorem is claimed.
