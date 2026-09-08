# Audit of the domino star--top shared-edge charge and the half-exponent residual

Date: 2026-07-27

Method: pure mathematics only.

## 0. Verdict

Let $F,G$ be simple domino-twin packets of rank

\[
 R=2r+1,
 \qquad n=2m,
 \qquad K=4m,
\]

and put $H=F\cap G$.  The local star-to-top ambiguity has the
following exact resolution.

1.  If two members of an $F$-star are a **genuine top-only edge** of
    $G$, the two endpoint mates left by the known top carrier are
    separately chargeable.  A mate is undetermined only if the
    adjacent $G$-star has exactly one member in $H$; that star then
    contains exactly three members of $G\setminus F$.  No singleton
    star receives two such charges.  Thus this branch has the sharp
    local cost
    \[
       3\text{ missing targets per free element label}.              \tag{0.1}
    \]

2.  If the common edge is a **hinge edge**, its two omitted labels are
    one endpoint domino of the $G$-top.  The other endpoint domino may
    be a wholly free two-set.  The exact local table is
    \[
    \begin{array}{c|c|c}
    \text{common targets in its adjacent }G\text{-star}
       &\text{remaining choices}&\text{noncommon targets}\\ \hline
    0&O(n^2)&4\\
    1\text{ on the free port}&O(n)&3\\
    1\text{ on the other port}&1&3\\
    \ge2&1&\le2 .
    \end{array}                                                        \tag{0.2}
    \]
    Hence the zero-common case has exactly the critical local exponent
    (2/4=1/2).  It cannot be replaced by a phase bit.

3.  The critical case is genuine globally.  Two independently
    repartitioned domino segments at displacement (r) have nearly
    coincident remote collars because
    \[
                         2r=m-(q_0+1).
    \]
    Their list exponent tends to $1/2$.  Consequently a uniform bound
    \[
      \#\{G:|F\setminus G|\le s\}
      \le \exp(O(m))n^{cs},\qquad c<1/2,                              \tag{0.3}
    \]
    is false for $s=o(m)$.

Thus the three-target split-mate charge is valid, but it does not prove
the requested close-neighbour theorem.  The whole-domino hinge branch,
and equivalently the paired (r)-separated front collision, is the
sharp surviving obstruction.

## 1. Alternating star--top normal form

Write the domino word of $G$ as

\[
 C_0,C_1,\ldots,C_{m-1},\qquad |C_i|=2,
\]

and put

\[
 W_i=C_i\cup\cdots\cup C_{i+r-1},
 \qquad U_i=W_i\cup C_{i+r}.
\]

The lower star and upper top at position (i) are

\[
 \mathcal S_i(G)
 =\{W_i+z:z\in C_{i-1}\cup C_{i+r}\},                  \tag{1.1}
\]

\[
 \mathcal T_i(G)
 =\{U_i-z:z\in C_i\cup C_{i+r}\}.                     \tag{1.2}
\]

The two endpoint dominoes $C_i,C_{i+r}$ partition the four facets in
(1.2) into two ports.  The port belonging to an endpoint $D$ is

\[
                         \{U_i-z:z\in D\}.             \tag{1.3}
\]

It is also a port of the adjacent star whose core is $U_i\setminus D$.
The star cells partition $G$, and their ports partition $G$ into
$2m$ disjoint two-sets.  The top cells give a second partition of the
same targets.

Let an $F$-star have core $A$ and let two of its members in $H$ be

\[
                         X=A+x,\qquad Y=A+y.            \tag{1.4}
\]

If they lie in one $G$-top, its carrier is forced:

\[
                         U=X\cup Y=A\cup\{x,y\}.        \tag{1.5}
\]

Moreover $U\setminus X=\{y\}$ and $U\setminus Y=\{x\}$, so $x,y$
are two of the four endpoint labels of that top.  There are exactly two
cases: they belong to different endpoint dominoes or to the same one.

## 2. Split endpoints: the exact three-target charge

Assume first that $x,y$ lie in different endpoint dominoes.  After
renaming the shores, write

\[
                         D_x=\{x,p\},\qquad D_y=\{y,q\}. \tag{2.1}
\]

The $D_x$-port contains $Y=U-x$, and its adjacent star has core

\[
                         K_x=U\setminus\{x,p\}.         \tag{2.2}
\]

Similarly the $D_y$-port contains $X=U-y$, and the other adjacent
star has core $K_y=U\setminus\{y,q\}$.

### Lemma 2.1 (free split mate implies a singleton star)

The label $p$ is determined by $U$ and $H\cap\mathcal S_x(G)$
unless

\[
                         H\cap\mathcal S_x(G)=\{Y\}.    \tag{2.3}
\]

In the exceptional case $\mathcal S_x(G)$ contains exactly three
targets of $G\setminus F$.  The analogous statement holds for $q$.

#### Proof

Suppose $Z\ne Y$ is another common target in the same $G$-star.
Two distinct members of a star have intersection equal to its core, so

\[
                         K_x=Y\cap Z.                   \tag{2.4}
\]

Equations (1.5), (2.2), and (2.4) then give

\[
                         \{x,p\}=U\setminus K_x,
 \qquad
                         p=(U\setminus K_x)\setminus\{x\}.             \tag{2.5}
\]

Thus $p$ is forced.  If no such $Z$ exists, the star has precisely
one common target and hence precisely three noncommon targets.  \(\square\)

The argument includes both possible locations of $Z$.  If $Z=U-p$
is the other member of the same port, (2.4) still applies.  If $Z$ is
on the other port, the same intersection again gives the star core.
There is no exceptional equality case.

### Lemma 2.2 (charges do not collide)

The two mates $p,q$ in (2.1) charge distinct singleton stars.  More
generally, one singleton $G$-star cannot be charged by two split mates.

#### Proof

The two endpoint ports of one top have two distinct adjacent stars.
For the global assertion, a singleton star has its unique common target
in exactly one of its two disjoint ports.  A split-mate charge through
the other port would supply a second common target, contradicting the
singleton assumption.  Also every target belongs to exactly one top
port, so the same common target cannot generate a second charge.  \(\square\)

Consequently, if $f_{\rm split}$ endpoint mates remain genuinely
undetermined after all common targets are exposed, then

\[
                         3f_{\rm split}
 \le |G\setminus F|=|F\setminus G|.                    \tag{2.6}
\]

This is the rigorous content of the proposed three-target charge.
Notice that the top union and the split/hinge bit alone do **not** fix
$p,q$; without Lemma 2.1 there are $O(n^2)$ choices.

## 3. Hinge endpoints: the exact critical table

Now assume $x,y$ form one endpoint domino

\[
                         E=\{x,y\}.                     \tag{3.1}
\]

Then the common edge is a port of the top and of the adjacent star.
Indeed

\[
                         U\setminus E=A,                \tag{3.2}
\]

so this is simultaneously the star realization with core (A).  Let

\[
                         \Lambda=\{p,q\}\subset A       \tag{3.3}
\]

be the other endpoint domino of the top, and let
$\mathcal S_\Lambda(G)$ be its adjacent star.  Its core is

\[
                         K=U\setminus\Lambda.           \tag{3.4}
\]

The $\Lambda$-port is

\[
                         P_\Lambda=\{U-p,U-q\}.         \tag{3.5}
\]

### Lemma 3.1 (hinge table)

Conditional on $U,E$ and the common targets in
$\mathcal S_\Lambda(G)$, the four rows of (0.2) hold.

#### Proof

If both targets in (3.5) are common, then

\[
                         \Lambda=(U-p)\triangle(U-q),   \tag{3.6}
\]

so it is fixed.  If exactly one, say (U-p), is common and there is no
common target on the other port, then (p=U\setminus(U-p)) is fixed and
only (q) remains, giving at most (n) choices.

If $Z$ on the other port is common, then that port uses a domino
disjoint from all blocks of (U).  Hence

\[
                         U\cap Z=K,                     \tag{3.7}
\]

and (3.4) fixes $\Lambda=U\setminus K$.  This also covers a mixture of
one common target on each port.  Thus every case with at least two
common targets is fixed, as is the one-common case in which the common
target is on the other port.

If the star is empty of common targets, no member of $\Lambda$ is
exposed locally.  There are at most

\[
                         \binom{|A|}{2}=\binom{2r}{2}=O(n^2)           \tag{3.8}
\]

possibilities, and all four members of the star lie in $G\setminus F$.
This proves the table.  \(\square\)

The zero-common row is not a bookkeeping artifact.  Locally one may
choose an arbitrary two-set $\Lambda\subset A$, partition
$A\setminus\Lambda$ into the remaining internal dominoes, and keep
the known hinge $E$.  Thus the $n^2$ scale is real before global
closure is imposed.

More explicitly, choose the other boundary domino of the star on the
$E$-port to be the second boundary domino of the original $F$-star.
That adjacent $G$-star is then the entire four-target $F$-cell.  The
choice of $\Lambda\subset A$ is still unrestricted by this collar, and
the star on the $\Lambda$-port may have no common target.  Hence one may
have four common targets on the hinge shore, zero on the free shore,
$\Theta(n^2)$ local choices for $\Lambda$, and exactly four missing
targets in the immediate free-shore star.  This realizes the critical
row of (0.2), rather than merely bounding it.

A zero star cannot support two independent whole-domino choices when
both neighbouring top carriers are known.  If those carriers are
$U_-,U_+$, then their endpoint blocks are disjoint and

\[
 K=U_-\cap U_+,
 \qquad
 U_-\setminus K, U_+\setminus K                         \tag{3.9}
\]

are the two endpoint dominoes.  This useful local fact still does not
give a uniform global saving, because long paired front families share
their closure collars.

## 4. The globally aligned half-exponent obstruction

For completeness, here is the exact calculation which prevents the
local charges from being summed into (0.3).  In the annular regime put

\[
 R=m-q_0=2r+1,
 \qquad h=m-2r=q_0+1=\Theta(\sqrt m).                   \tag{4.1}
\]

Fix two domino-position intervals

\[
 I=\{0,\ldots,\ell-1\},
 \qquad J=I+r,                                          \tag{4.2}
\]

where $1\ll\ell$, $\ell+h<r$.  Independently repartition the
$2\ell$ labels in each interval into an ordered list of $\ell$
unordered dominoes, keeping all other dominoes fixed.  The number of
distinct simple supports is at least

\[
 {1\over2m}\left({(2\ell)!\over2^\ell}\right)^2.       \tag{4.3}
\]

Indeed a simple support recovers its domino necklace, so only one of
the (2m) global dihedral symmetries can identify two displayed words.

Put (L=\{1,\ldots,\ell-1\}).  The starts of cores which can change
under the first repartition are (L\cup(L-r)); those for the second
are ((L+r)\cup L).  Therefore their union is

\[
                         L\cup(L-r)\cup(L+r).            \tag{4.4}
\]

The middle band is disjoint from the other two.  Since

\[
                         2r\equiv-h\pmod m,              \tag{4.5}
\]

the two remote bands have union size

\[
                         (\ell-1)+\min\{\ell-1,h\}.
\]

Thus (4.4) has size

\[
                         2(\ell-1)+\min\{\ell-1,h\}.    \tag{4.6}
\]

There are at most four further cells whose core is unchanged but whose
boundary domino meets one of the two modified intervals.  Every other
four-target cell is literally unchanged.  Hence every constructed
packet satisfies

\[
 |F\setminus G|
 \le s_\ell:=8\ell+4\min\{\ell-1,h\}+8.               \tag{4.7}
\]

On the other hand, Stirling's formula gives

\[
 \log |\mathcal F_\ell|
 =4\ell\log\ell+O(\ell+\log m).                        \tag{4.8}
\]

Take $\ell=m/\sqrt{\log m}$.  Then $h=o(\ell)=o(m)$, the right side
of (4.7) is ((8+o(1))m/\sqrt{\log m}=o(m)), and

\[
 \frac{\log |\mathcal F_\ell|}
      {s_\ell\log n}
 \ge {1\over2}-o(1).                                   \tag{4.9}
\]

For every fixed (c<1/2), the gap between (4.8) and
(c|F\setminus G|\log n) is (Omega(m\sqrt{\log m})), which cannot be
absorbed by an $\exp(O(m))$ prefactor.  This proves the failure of
(0.3).

There is also an exact terminal-scale consequence.  For

\[
 s_A=\left\lceil {A m\over\log m}\right\rceil,
 \qquad
 \ell=\left\lfloor {s_A-4h-8\over8}\right\rfloor,
\]

write

\[
 B_s(F)=\{G:|F\setminus G|\le s\}.
\]

The same family lies inside the (s_A)-ball and satisfies

\[
 \log |B_{s_A}(F)|
 \ge {A\over2}m
 -{A\over2}{m\log\log m\over\log m}
 -O_A\!\left({m\over\log m}\right).                  \tag{4.10}
\]

Therefore a bound

\[
 |B_{s_A}(F)|\le \exp(C_*m+o(m))n^{c s_A}
\]

necessarily has

\[
                         C_*\ge(1/2-c)A.              \tag{4.11}
\]

So an additive exponential constant uniform in (A) cannot later be
beaten simply by choosing (A) larger.  The full derivation, including
the exact constant (8) in the defect budget, is recorded in the
independent double-segment audit.

## 5. Exact proved boundary

Proved here:

1. the complete split-versus-hinge classification of a shared
   star--top edge;
2. the injective three-target charge for every genuinely free split
   endpoint mate;
3. the exact hinge table, including the $O(n^2)$-choice, four-defect
   whole-domino row;
4. the noncollision facts for singleton-star charges and doubly anchored
   zero stars; and
5. the globally aligned double-segment construction refuting every
   uniform exponent (c<1/2).

Not proved, and not implied by the local charge:

1. a terminal estimate at one prescribed scale
   (s=A m/\log m) whose explicit additive constant meets the necessary
   lower bound (4.11);
2. a dynamic residual-link theorem excluding simultaneous survival of
   the two (r)-separated repartitions; or
3. an annular near-factor or coefficient-one conclusion.

The exact next static statement is therefore a clustered estimate which
treats the two (r)-separated moving fronts as one object.  A raw
missing-target list estimate cannot have the required strict power
margin.
