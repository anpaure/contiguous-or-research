# Mixed PBBS/product-SCD Gaussian-annulus coupling: exact input audit

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

There are two different meanings of "sharing the baseline", and they have
opposite answers.

1. The two already constructed literal words cannot be overlaid, even after
   arbitrary reordering of the product-SCD gadgets.  At a sub-Gaussian
   cutoff the odd product-SCD word itself has length

   \[
      (2\sqrt2+o(1))\binom{2m+1}{m}.
   \]

   Moreover its letters and the principal PBBS erosion letters have
   disjoint cardinality ranges.  Hence an exact common-supersequence or
   position-identification fusion cannot have coefficient one.

2. If one forgets the literal product-SCD carrier and retains only the
   statewise containment flags at one depth, there is no integral Hall
   obstruction at all.  For every perfect middle matching, including the
   PBBS matching, all lower and upper targets at that depth can be coupled
   through one common set of middle edges.  The exact necessary-and-
   sufficient inequality is Edmonds' common-base cut

   \[
      r_q^-(A)+r_q^+(E\setminus A)\ge D_q
      \qquad(A\subseteq E),                         \tag{0.1}
   \]

   and it always holds in the unrestricted Boolean inclusion graph.

Thus the first genuinely live mixed gate is neither a scalar endpoint
count nor a one-depth Hall condition.  It is the same common-base condition
after imposing the fixed product-SCD carrier and PBBS erosion provenance,
simultaneously at all depths with nested literal chronology.  The orbit
argument proving (0.1) does not survive those restrictions.

## 1. Exact quantifiers and floors

Put

\[
 n=2m+1,\qquad W_o=\binom{2m+1}{m},\qquad
 W_e=\binom{2m}{m},\qquad B=\operatorname {Cat}_m={W_o\over n}.
\tag{1.1}
\]

For the even product-SCD word, with

\[
 h_0=\lfloor m/2\rfloor,\quad \epsilon=m-2h_0,
 \quad x=h_0-a,\quad d=H+1-\epsilon,
\]

the exact length is

\[
 L_m(m-H-1)
 =2\sum_{x=0}^{h_0}B_{m,x}
   \binom m{h_0-(d-x)_+},                            \tag{1.2}
\]

where \(B_{m,x}=A_m(h_0-x)w_m(h_0-x)\) and

\[
 \sum_xB_{m,x}=2^m-1.                               \tag{1.3}
\]

If \(H/\sqrt m\to c<\infty\), then

\[
 {L_m(m-H-1)\over W_e}\longrightarrow
 F(c),                                               \tag{1.4}
\]

where

\[
 F(c)=2\sqrt2\int_0^\infty
 8\sqrt{2/\pi}\,y^2e^{-2y^2}e^{-2(c-y)_+^2}\,dy>0.
\tag{1.5}
\]

In particular \(F(0)=2\sqrt2\).  The trimmed odd lift has length
\(2L_m(m-H-1)\), and since \(W_o\sim2W_e\), its normalized limit is
again \(F(c)\).  Therefore the exact product-SCD exterior word is
\(o(W_o)\) if and only if \(H/\sqrt m\to\infty\).

The PBBS theorem has a different quantifier.  For every integer
\(h\ge1\) with \(h=o(\sqrt m)\), use compiler parameter

\[
 H_c=h+1.                                            \tag{1.6}
\]

The resulting literal word has length

\[
 W_o+O(Bh\sqrt m)=W_o\bigl(1+O(h/\sqrt m)\bigr)
 =W_o+o(W_o),                                        \tag{1.7}
\]

and covers the paired ranks

\[
 \binom{[n]}{m-q}\cup\binom{[n]}{m+1+q},
 \qquad0\le q\le h.                                \tag{1.8}
\]

It actually covers the additional upper rank \(m+h+2\).  The odd
product tail with parameter \(H=h\) covers ranks at most \(m-h-1\)
and at least \(m+h+2\).  Thus the ranks meet, but the costs do not: the
separately appended tail has normalized cost \(2\sqrt2+o(1)\).

For later use, the exact size of either signed depth-\(q\) layer is

\[
 D_q=\binom{2m+1}{m-q},
 \qquad
 {D_q\over W_o}
 =\prod_{j=0}^{q-1}{m-j\over m+2+j}.                \tag{1.9}
\]

Consequently

\[
 \log {D_q\over W_o}
 =-{q(q+1)\over m}
  +O\!\left({q^2\over m^2}+{q^4+1\over m^3}\right)
 \quad(q=O(\sqrt m)),                               \tag{1.10}
\]

so \(D_q/W_o=1-o(1)\) for \(q=o(\sqrt m)\), whereas
\(D_q/W_o\to e^{-A^2}\) for \(q=A\sqrt m+O(1)\).

## 2. A literal-overlay no-go for the two existing words

Every letter in the even product-SCD word is either a singleton or the
minimum member of one half-cube symmetric chain.  Hence its cardinality
is at most \(\lfloor m/2\rfloor\).  In the trimmed odd lift, a letter is
an old letter, \(\{z\}\), or an old letter with \(z\) adjoined.  Thus

\[
 |Q|\le\lfloor m/2\rfloor+1                         \tag{2.1}
\]

for every product-tail letter.

The principal PBBS letters at compiler radius \(H_c\) are

\[
 D_i=\bigcap_{j=0}^{H_c}\widetilde X_{i+j},          \tag{2.2}
\]

where consecutive \(m\)-sets differ by one Johnson exchange.  Starting
from \(\widetilde X_i\), at most one of its elements can disappear per
step, and therefore

\[
 |D_i|\ge m-H_c.                                     \tag{2.3}
\]

When \(H_c=o(\sqrt m)\), eventually

\[
 m-H_c>\lfloor m/2\rfloor+1.                        \tag{2.4}
\]

Thus no principal PBBS baseline letter equals a letter of the exact odd
product-SCD word.

The PBBS word has \(W_o\) principal baseline positions and only
\(o(W_o)\) auxiliary positions by (1.7).  A common-supersequence overlay
can identify two positions only when their literal set labels agree.
Equations (2.1)--(2.4) show that at most \(o(W_o)\) product-tail positions
can be identified with the PBBS word.  Hence every fusion which preserves
both already constructed words as literal subsequences has length at
least

\[
 W_o+2L_m(m-h-1)-o(W_o)
 =(1+2\sqrt2-o(1))W_o.                               \tag{2.5}
\]

This is a statewise no-go for direct overlay.  It does not obstruct a new
word which dismantles the product gadgets and uses only their states or
flags.

### Theorem 2.1 (sparse-edit endpoint obstruction)

Let a PBBS central word have \(W_o\) distinguished principal positions
and \(a\) other positions. Fix a target depth \(H\), and suppose that a
new word is obtained while

* leaving all but \(r\) principal positions unchanged;
* inserting \(s\) new positions; and
* leaving every unchanged principal letter of cardinality strictly larger
  than \(m-H\).

If the new word covers every member of
\(\binom{[2m+1]}{m-H}\), then

\[
 \boxed{r+s+a\ge D_H,\qquad
        D_H=\binom{2m+1}{m-H}.}                     \tag{2.6}
\]

In particular, when the old central excess is \(a=o(W_o)\),

\[
 \boxed{r+s\ge D_H-o(W_o).}                         \tag{2.7}
\]

#### Proof

Choose one witnessing interval for every rank-\((m-H)\) target and map
the target to the right endpoint of its witness.  Two distinct targets of
the same rank cannot have the same right endpoint: intervals with a common
right endpoint are nested as their left endpoints move, hence their unions
are comparable, and two comparable sets of equal size are equal.

No chosen witness can end at an unchanged principal position.  Such a
witness contains its endpoint letter, whose cardinality is larger than
\(m-H\), so its union cannot have cardinality \(m-H\). Therefore all
\(D_H\) distinct right endpoints lie among the at most \(r\) altered
principal positions, the \(s\) inserted positions, and the \(a\) old
nonprincipal positions.  This proves (2.6), and (2.7) follows. \(\square\)

The exact density in (2.6) is

\[
 {D_H\over W_o}
 =\prod_{j=0}^{H-1}{m-j\over m+2+j},                \tag{2.8}
\]

and, uniformly for \(H=O(\sqrt m)\),

\[
 \log {D_H\over W_o}
 =-{H(H+1)\over m}
  +O\!\left({H^2\over m^2}+{H^4+1\over m^3}\right).
                                                        \tag{2.9}
\]

Hence sparse editing is impossible in either relevant regime:

\[
 \begin{array}{ll}
 H=o(\sqrt m):
   &r+s\ge(1-o(1))W_o,\\[1mm]
 H=A\sqrt m+O(1):
   &r+s\ge(e^{-A^2}-o(1))W_o.
 \end{array}                                        \tag{2.10}
\]

The strict-cardinality hypothesis contains an important floor. If the
principal radius is \(R\), meaning

\[
 D_i^{(R)}=\bigcap_{j=0}^{R}\widetilde X_{i+j},
\]

then only

\[
 |D_i^{(R)}|\ge m-R                                \tag{2.11}
\]

is automatic. Theorem 2.1 applies to depth \(H\) whenever

\[
 R\le H-1,                                          \tag{2.12}
\]

because then \(m-R\ge m-H+1\). It does **not** apply merely from
cardinality when \(R=H\): an \(H\)-safe principal letter then has size
exactly \(m-H\) and may itself be a target.

For the sub-Gaussian theorem stated in Section 1, the compiler radius is
\(R=H_c=h+1\). Its first uncovered lower rank is \(m-h-1=m-R\), so the
strict inequality fails exactly at that first boundary.  The sparse-edit
obstruction applies to every deeper annulus rank \(m-H\) with
\(H\ge h+2\). Thus it proves that a mixed construction reaching a
Gaussian depth cannot preserve all but \(o(W_o)\) of the sub-Gaussian
PBBS baseline; it must perform a linear-scale rethreading.  It does not by
itself obstruct a specially designed coupling at the single first
boundary rank.

## 3. The smallest unrestricted one-depth integral coupling

Let

\[
 \pi:\binom{[n]}m\longrightarrow\binom{[n]}{m+1}
\]

be any perfect matching with \(X\subset\pi(X)\).  Let \(E\) be its
\(W_o\) edges, writing \(e=(X_e,Y_e)\).  A PBBS middle shore supplies
such a matching.

At depth \(q\), put

\[
 \mathcal L_q=\binom{[n]}{m-q},\qquad
 \mathcal U_q=\binom{[n]}{m+1+q}.                   \tag{3.1}
\]

Define two transversal matroids on the common ground set \(E\).

* A set \(I\subseteq E\) is independent in \(M_q^-\) if its edges can
  be matched injectively to distinct \(S\in\mathcal L_q\) satisfying
  \(S\subset X_e\).
* A set \(I\subseteq E\) is independent in \(M_q^+\) if its edges can
  be matched injectively to distinct \(T\in\mathcal U_q\) satisfying
  \(Y_e\subset T\).

Both matroids have rank \(D_q\).  A common base \(J_q\) is exactly a set
of \(D_q\) PBBS middle edges for which there are bijections

\[
 \mathcal L_q\longleftrightarrow J_q
 \longleftrightarrow\mathcal U_q,                   \tag{3.2}
\]

and every resulting triple is the nested flag

\[
 S\subset X_e\subset Y_e\subset T.                 \tag{3.3}
\]

### Theorem 3.1 (one-depth common carriers always exist)

For every \(m,q\) and every perfect middle matching \(\pi\), the two
matroids \(M_q^-\) and \(M_q^+\) have a common base.  Equivalently,

\[
 \boxed{
 r_q^-(A)+r_q^+(E\setminus A)\ge D_q
 \quad\hbox{for every }A\subseteq E.}               \tag{3.4}
\]

#### Proof

The inclusion graph between \(\mathcal L_q\) and the rank-\(m\) sets is
biregular.  A lower vertex has degree

\[
 \binom{m+1+q}{q},
\]

and a middle vertex has degree \(\binom mq\).  Edge counting gives Hall's
inequality, so a matching saturating \(\mathcal L_q\) exists.  Thus
\(M_q^-\) has a base of size \(D_q\).  Permuting the ground coordinates
and averaging the orbit of one base gives the uniform vector

\[
 x_e={D_q\over W_o}\qquad(e\in E)                   \tag{3.5}
\]

in the base polytope of \(M_q^-\).  In particular, for every
\(A\subseteq E\),

\[
 r_q^-(A)\ge {D_q\over W_o}|A|.                     \tag{3.6}
\]

The upper inclusion graph has the same argument.  Averaging on the
rank-\((m+1)\) shore and pulling back through the arbitrary bijection
\(e\mapsto Y_e\) again gives the same uniform vector, hence

\[
 r_q^+(E\setminus A)
 \ge {D_q\over W_o}|E\setminus A|.                  \tag{3.7}
\]

Adding (3.6)--(3.7) proves (3.4).  The matroid-intersection min-max theorem
says that the maximum common independent-set size is

\[
 \min_{A\subseteq E}
 \bigl(r_q^-(A)+r_q^+(E\setminus A)\bigr).
\]

It is therefore at least \(D_q\), and neither matroid has larger rank.
The common independent set is a common base, proving (3.2)--(3.3).
\(\square\)

At the first rank beyond a sub-Gaussian PBBS band, \(q=h+1\), this theorem
uses

\[
 |J_q|=D_q=(1-o(1))W_o.                              \tag{3.8}
\]

Thus the endpoint-counting requirement that almost every middle carrier
participate is integrally feasible at one depth.  No dual witness which
sees only Boolean containment can obstruct the mixed construction.

## 4. The hidden carrier mismatch

Theorem 3.1 deliberately forgets the product-SCD carrier.  In the exact
tail word a target belongs to the unique ordered pair of half-cube chains
containing its two coordinate projections, and its witness must be a
suffix of the first chain word followed by a prefix of the second.  A
PBBS erosion position has, in addition, a prescribed owner window and
canonical provenance interval.  Mere containment (3.3) certifies none of
these facts.

Let \(R_q^-\subseteq\mathcal L_q\times E\) and
\(R_q^+\subseteq E\times\mathcal U_q\) be the actual allowed relations
after imposing:

1. the same product-SCD chain-pair context;
2. the correct literal suffix/prefix endpoint in that gadget;
3. the PBBS signed owner and erosion-provenance condition; and
4. the chosen physical orientation.

Let \(\widehat M_q^\pm\) be the resulting transversal matroids.  Then the
smallest exact one-depth integral gate is

\[
 \boxed{
 \widehat r_q^-(A)+\widehat r_q^+(E\setminus A)\ge D_q
 \quad(A\subseteq E).}                              \tag{4.1}
\]

This condition is necessary and sufficient for a common set of integral
carriers at depth \(q\).  A single set \(A\) violating (4.1) is a genuine
statewise no-go.  The proof of Theorem 3.1 cannot be reused: a fixed SCD,
a fixed PBBS matching, and fixed erosion provenance are not jointly
coordinate-transitive, so the common uniform point need not lie in either
restricted base polytope.

There is a useful coarser form of this cut which is completely explicit.
In even dimension, a product context is an ordered pair of half chains
with minimum ranks (a,b).  Its number of rank-(r) states is

\[
 d_{a,b}(r)=
 \left[
  \min(m-a,r-b)-\max(a,r-m+b)+1
 \right]_+,                                         \tag{4.2}
\]

while its number of middle states is

\[
 c_{a,b}=m-2\max(a,b)+1.                            \tag{4.3}
\]

The symmetric upper rank (2m-r) has the same count as (4.2).  Form the
bipartite multigraph whose left vertices are the product contexts of the
lower/middle shore, whose right vertices are the contexts of the
middle/upper shore, and whose edges are the actual PBBS middle edges.
If (d_u,d_v) are the corresponding boundary demands, a common carrier
set respecting contexts can exist only if, for every left-context set
(P) and right-context set (Q),

\[
 \boxed{
  \sum_{u\in P}d_u
  \le e(P,V\setminus Q)+\sum_{v\in Q}d_v.}          \tag{4.4}
\]

Conversely (4.4), together with equality of the total two-shore demands,
is sufficient for selecting edges with exactly those context degrees: it
is the integral max-flow/min-cut theorem with unit capacities on the PBBS
edges.  It is not sufficient for the literal construction, since the
selected states inside each context must still support the actual target
matching and suffix/prefix ports.  Nevertheless, a violation of (4.4) is
already a canonical context-level statewise no-go.

Even (4.1) at every depth is not the all-depth theorem.  The chosen
carriers and their assigned targets must be nested along one literal
chronology.  If \(\Gamma_e\) denotes the legal complete lower/upper
annulus towers at carrier \(e\), the fractional configuration condition
is

\[
 \sum_{e\in E}\max_{\gamma\in\Gamma_e}
       \langle w,a_{e,\gamma}\rangle
 \ge \langle w,\mathbf1\rangle
 \qquad(w\ge0),                                     \tag{4.5}
\]

where \(a_{e,\gamma}\) is the target-incidence vector of the tower.
Equation (4.5) is only the fractional Farkas condition.  The literal word
requires an integral selection of one tower per carrier, together with
the PBBS boundary order and erosion replacement provenance.  Fractional
orbit averaging does not supply that integral selection.

## 5. Audited boundary

The exact conclusions are therefore:

* the sub-Gaussian PBBS theorem and exact product-SCD tail have no
  economical cutoff overlap;
* the two existing literal words cannot be merged by identifying their
  letters or by retaining the product word as a subsequence;
* unrestricted one-depth lower/middle/upper endpoint coupling is always
  integrally feasible, for an arbitrary PBBS middle matching;
* the first possible obstruction is the restricted common-base cut
  (4.1), and the all-depth problem is the integral tower selection behind
  (4.5).

No annulus construction and no coefficient-one conclusion is claimed.
