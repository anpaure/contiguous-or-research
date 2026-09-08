# The relaxed projected-MSW low-switch gate: exact interval obstruction, abstract no-go, and shadow chronology

Date: 2026-07-26

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Put

\[
 p=2m+1\text{ prime},\qquad
 W=\binom pm,\qquad T=W/p=\operatorname {Cat}_m,
 \tag{0.1}
\]

and let \(H=o(p)\). Let \(F\) be an oriented exact MSW factor, and
project its tagged arcs to the two split shores of the \(T\) translation
necklaces. The resulting bipartite multigraph \(B_F\) is \(p\)-regular.

The requested actual-MSW theorem

\[
 \boxed{S_{\rm tag}(\chi)=o(pT/H)=o(W/H)}
 \tag{0.2}
\]

for a proper \(p\)-edge-colouring \(\chi\) is **not proved**, and no
actual-MSW lower bound contradicting (0.2) is proved. The exact advance is
the following six-part boundary.

1. The statistic which certifies literal long MSW chronology is the
   tagged row-switch count \(S_{\rm tag}\), not the weaker one-step
   active-orbit count. A formal \(p=5\) counterexample below has zero
   one-step orbit switches but leaves its original translated row after
   two arcs. The missing datum is an \(H\)-overlap root/phase cocycle.

2. If (0.2) holds, one colour matching has

   \[
                        r=o(T/H).                     \tag{0.3}
   \]

   There is a scale

   \[
                  H=o(L),\qquad L=o(p)               \tag{0.4}
   \]

   such that its complete rows and runs of length at least \(L\) contain
   \(T-o(T)\) selected quotient arcs. Their physical lifts are literal
   translated MSW segments. The discarded owner mass is \(o(W)\), the
   every-second Johnson chronology has at most \(T+2pr=o(W/H)\)
   components, and the common \(H\)-collar is \(o(W)\).

3. Let \(\Pi_L\) be the maximum total arc length of a split-shore-disjoint
   packing of admissible cyclic MSW-row intervals of length at least
   \(L\), with complete admissible rows allowed. Every proper colouring
   obeys the exact scale-sensitive obstruction

   \[
      \boxed{
      S_{\rm tag}(\chi)
      \ge {p\bigl(T-\Pi_L\bigr)\over L-1}}
      \qquad(2\le L\le p).                           \tag{0.5}
   \]

   Thus an actual-MSW estimate

   \[
            \Pi_{\lceil CH\rceil}\le(1-\delta)T      \tag{0.6}
   \]

   for fixed \(C,\delta>0\) would rigorously refute (0.2). Conversely,
   (0.2) forces \(\Pi_{\lceil CH\rceil}=T-o(T)\) for every fixed \(C\).
   No estimate (0.6) is presently known.

4. There is no fractional owner-Hall obstruction. After a favourable
   coordinate relabelling all but at most \(p(p-1)\) rows are
   necklace-transversal. On that core, giving every exact length-\(L\)
   interval weight \(1/(pL)\) is a fractional packing of owner weight
   \(T-O(p^2)\). The exact paired-shore codegree is nevertheless

   \[
      d(O_L)=pL,\qquad d(O_L,O_R)=p(L-1)
      \quad(1\le L<p),                                \tag{0.7}
   \]

   so a generic low-codegree nibble is unavailable. Any positive proof
   must round the highly correlated interval columns.

5. A universal positive theorem is false even after demanding simple
   transversal rows. There are \(p\)-regular directed quotient systems,
   decomposed into \(T\) directed simple \(p\)-cycles, for which every
   proper \(p\)-edge-colouring satisfies

   \[
            \boxed{S_{\rm tag}\ge {W\over3\log p}.} \tag{0.8}
   \]

   Since \(H/\log p\to\infty\) at the intended scale, (0.8) is much
   larger than \(W/H\). This abstract system is not asserted to be an
   MSW-voltage projection. It proves that regularity, row simplicity,
   recursive balanced \(b\)-factors, Euler pairings, and generic Kempe
   routing cannot prove (0.2).

6. Low switching controls chronology, not missing shadows. There is a
   new mixed-run shadow cut. For one colour matching \(M\), let
   \(R_{\le L_0}(M)\) be the total selected quotient-arc mass lying in
   partial tagged runs of length at most \(L_0\). Put

   \[
     \rho_q={1\over W}\binom p{m-q}
      =\prod_{j=0}^{q-1}{m-j\over m+2+j}.             \tag{0.9}
   \]

   If \(Q\le\min\{H,L_0/2\}\), then the aggregate two-sign target holes
   of the windows inherited wholly inside tagged runs satisfy

   \[
      \boxed{
      D^{\rm inh}_{\le Q}(M)
      \ge
      2\left[
      {Q^2\over L_0}R_{\le L_0}(M)
      -T\sum_{q=1}^Q(1-\rho_q)
      \right]_+.}                                    \tag{0.10}
   \]

   In particular, if \(H\ge c_0\sqrt m\), then throughout the Gaussian
   window direct inherited aggregate holes can be \(o(T)\) only if

   \[
      R_{\le L_0}(M)=o(T)
      \quad\text{for every }L_0\to\infty,\ 
             L_0=O(m^{2/3}).                          \tag{0.11}
   \]

   (For the chosen low-switch matching and bounded \(L_0\), the same
   conclusion follows directly from
   \(R_{\le L_0}\le L_0r=o(T)\).) Thus almost all selected mass must lie
   in complete rows or in partial runs longer than every fixed multiple
   of \(m^{2/3}\), unless a legal
   cross-boundary collar supplies the missing targets. This is a
   rigorous missing-shadow obstruction, not a lower bound on the switch
   count itself.

The smallest surviving positive statement is therefore an
**MSW-specific, extendable, shadow-covering long-interval packing**. A
full low-switch one-factorization is stronger than necessary: one quotient
perfect matching with (0.3), the root cocycle, and \(o(T)\) quotient
shadow deficiency already supplies the needed colour factor.

## 1. The exact tagged colouring model

Write the oriented arcs of an MSW row \(C\) as

\[
                e_{C,0},e_{C,1},\ldots,e_{C,p-1}      \tag{1.1}
\]

in cyclic order. Project every physical arc as a separate tagged edge of
\(B_F\); parallel tags are retained. A proper edge-colouring

\[
                 \chi:E(B_F)\longrightarrow\mathbb F_p              \tag{1.2}
\]

uses every colour exactly once at every left and every right necklace.
Consequently every colour class \(M_a\) is a quotient perfect matching and
has exactly \(T\) tagged edges.

Define

\[
 S_{\rm tag}(\chi)
 =\sum_C\sum_{i\in\mathbb Z_p}
   \mathbf1_{\{\chi(e_{C,i})\ne\chi(e_{C,i+1})\}}.     \tag{1.3}
\]

For a colour \(a\), decompose its selected positions on every row into
cyclic one-runs. A nonempty proper selected subset contributes its usual
number of cyclic runs; an empty or complete selected row contributes zero.
Let \(r_a\) be the aggregate resulting run count.

### Lemma 1.1 (exact run identity)

\[
                       \boxed{S_{\rm tag}(\chi)=\sum_{a}r_a.}          \tag{1.4}
\]

#### Proof

On a nonconstant cyclic colour word, the number of monochromatic runs is
exactly the number of colour changes. Its colour-\(a\) runs are precisely
the partial one-runs counted by \(r_a\). On a constant row both sides are
zero under the complete-row convention. Sum over the rows. \(\square\)

For one matching \(M=M_a\), put \(x_{C,i}=1\) when \(e_{C,i}\in M\) and
zero otherwise. Then the sharper binary identities are

\[
 \boxed{
 \begin{aligned}
 r(M)
 &=T-\sum_{C,i}x_{C,i}x_{C,i+1}\\
 &={1\over2}\sum_{C,i}|x_{C,i+1}-x_{C,i}|\\
 &={1\over2}\|(I-U)x\|_2^2,
 \end{aligned}}                                       \tag{1.5}
\]

where \(U\) shifts one tagged arc along every original row. Indeed a
partial binary cyclic word with \(k\) ones and \(r\) runs has \(k-r\)
adjacent \(11\)-pairs; a complete row has \(p\) of each and contributes
zero.

### Why the one-step orbit statistic is weaker

A directed translation-arc orbit may have more than one tag. If a colour
activates the orbit of the next tagged MSW arc through a different tag,
it preserves the next physical arc. It need not preserve the third arc,
because the new representative may have a different canonical successor
orbit.

Here is an exact formal example. Let

\[
                    V=\mathbb Z_5\times\mathbb Z_5,
 \qquad \tau(q,g)=(q,g+1).                            \tag{1.6}
\]

For every phase \(g\), make \(F\) the root cycle

\[
 (g,g)\to(g+1,g)\to(g+2,g)\to(g+4,g)\to(g+3,g)\to(g,g).          \tag{1.7}
\]

The five tags based at \(x_i=(i,i)\) project to a quotient perfect
matching; their lift is

\[
                        \widetilde F(i,h)=(i+1,h).     \tag{1.8}
\]

For every \(i\), the arc tagged at \(x_{i+1}\) is a translate of the
canonical continuation after the arc tagged at \(x_i\). Hence every
one-step active-orbit switch indicator is zero. Nevertheless the lifted
root word begins

\[
                           0,1,2,3,                           \tag{1.9}
\]

whereas an original \(F\)-row has cyclic difference word

\[
                           1,1,2,4,2.                         \tag{1.10}
\]

No three-arc lifted prefix in (1.9) lies in one translated original row.
The selected matching extends to a proper \(5\)-edge-colouring because
its complement in the tagged quotient graph is \(4\)-regular bipartite.

The example can retain the formal omission-rainbow property of every old
row. Give the normalized \(q\to q+1\), \(q\to q+2\), and \(q\to q-1\)
translation-orbit families the label arrays

\[
 A=(0,1,0,1,2),\qquad
 B=(3,4,3,2,4),\qquad
 C=(3,2,0,1,4).                                      \tag{1.10a}
\]

At phases \(g=0,1,2,3,4\), the five old-row label words are respectively

\[
 01324,\quad10243,\quad01432,\quad12340,\quad20431,   \tag{1.10b}
\]

all permutations of \(\mathbb Z_5\). Translation adds the common phase
to every label. The zero-orbit-switch lift (1.8), however, has phase-zero
label word \(A=01012\), already repeating in its first three arcs. Thus
one-step orbit preservation does not even preserve formal short-window
label distinctness.

The exact repair is a rooted overlap cocycle. Suppose the next selected
representative \(z\) and the carried root \(x\) satisfy, for a unique
phase \(u\),

\[
                  (z,Fz)=\tau_u(Fx,F^2x).             \tag{1.11}
\]

One-step orbit activity asserts only (1.11). Literal \(H\)-step
continuation requires

\[
            \boxed{F^jz=\tau_uF^{j+1}x
                   \quad(0\le j\le H).}              \tag{1.12}
\]

This is the de Bruijn \(H\)-overlap condition on rooted row prefixes and
suffixes. A tagged monochromatic run enforces the stronger section
\(z=Fx\), and hence (1.12) at every internal junction. Alternatively one
may carry \(x\leftarrow Fx\) statefully and cut only when its required
next orbit is inactive. That stateful failure count is trajectory
dependent and is not the static one-step orbit statistic.

The example is a formal translation/row system, not an embedding into the
actual odd graph. Its role is logical: multi-step chronology does not
follow from one-step orbit activity without (1.12).

## 2. Relaxed switches give genuinely long literal segments

### Theorem 2.1 (long tagged-run extraction)

Assume

\[
                    HS_{\rm tag}(\chi)=o(pT).          \tag{2.1}
\]

Then some colour \(a\) has \(r=r_a=o(T/H)\). There is an integer \(L\)
satisfying (0.4) such that deleting tagged partial runs of length less
than \(L\) removes \(o(T)\) selected quotient arcs. Every remaining
partial run and complete row lifts to literal translated MSW segments.

#### Proof

Lemma 1.1 and averaging give \(r\le S_{\rm tag}/p=o(T/H)\). Put

\[
                        \delta={Hr\over T}=o(1).       \tag{2.2}
\]

If \(r=0\), take \(L=\lfloor\sqrt{Hp}\rfloor\). Otherwise take, with
harmless integer rounding,

\[
            L=H\min\{\delta^{-1/2},(p/H)^{1/2}\}.     \tag{2.3}
\]

Both quantities inside the minimum tend to infinity, so \(L/H\to\infty\).
Also \(L\le\sqrt{Hp}\), hence \(L/p\to0\). Finally

\[
 {Lr\over T}={L\over H}\delta=o(1):                   \tag{2.4}
\]

in the first branch it is at most \(\sqrt\delta\), while in the second
branch the branch condition gives \(\delta\le H/p\), and the expression is
at most \(\sqrt{H/p}\).

There are \(r\) partial runs, so their total mass below \(L\) is less than
\(Lr=o(T)\). Inside a tagged run the selected tags are literally
\(e_X,e_{FX},\ldots\); their translation lifts therefore follow one fixed
translated MSW row. \(\square\)

### Exact physical ledger

Let \(f\) be the number of complete tagged rows in the chosen colour.
They are split-shore disjoint, so

\[
                             pf\le T.                 \tag{2.5}
\]

Declare a cut after every partial tagged run. Parallel tags cannot have
the same colour, so these \(r\) quotient cuts lift to exactly

\[
                             b=pr                    \tag{2.6}
\]

distinct declared physical cuts. Some may be phantom physical seams
because an alternate active orbit happens to continue the factor; keeping
them only strengthens the chronology certificate.

For either parity, a depth-\(q\) every-second window uses \(2q\) odd arcs.
Therefore the exact declared bad-start bound is

\[
                   |D_q^\pm|\le(2q-1)b.              \tag{2.7}
\]

At fixed maximal depth the two parities together use at most
\(2(2H-1)b\) bad starts. The raw two-sign, all-depth sum is at most

\[
                2b\sum_{q=1}^H(2q-1)=2H^2b.          \tag{2.8}
\]

The latter is an occurrence count, not the word toll of a common collar.
A single copied length-\(H\) neighbourhood can reproduce the whole
triangular flag family at one boundary; one must not pay an independent
length-\(H\) word at every depth.

After every-second traversal, the \(b\) cut odd transitions give at most
\(2b\) open Johnson paths. Complete tagged rows lift to \(pf\le T\)
seam-free Johnson cycles. Hence

\[
                        K_J\le T+2b.                 \tag{2.9}
\]

A conservative componentwise full-collar charge is

\[
                   (2H+1)(T+2b)=o(W),                \tag{2.10}
\]

because \(HT=o(pT)=W\) and \(Hb\le H S_{\rm tag}=o(W)\). The sharper
shared-boundary convention gives

\[
                   2(H+1)b+(2H+1)T,                  \tag{2.11}
\]

before positive-depth target-hole repair. Finite two-sign row safety
requires \(2H+2\le p\), which follows eventually from \(H=o(p)\).

The short-run deletion in Theorem 2.1 costs \(pLr=o(W)\) physical middle
owners. Before every-second traversal, the remaining open odd segments
and full odd cycles number at most

\[
                   pr+pf\le pr+T=o(W/H).             \tag{2.12}
\]

After every-second traversal the corresponding bound is \(2pr+T\), as
in (2.9). Thus the relaxed switch estimate is exactly strong enough for the
component, reset, and literal \(H\)-chronology ledgers.

## 3. The exact mesoscopic interval obstruction

Split every quotient necklace into a left and a right resource. A cyclic
interval \(I\) of an MSW row is **admissible** if its tagged arcs form a
matching in \(B_F\), equivalently if its tail necklaces are distinct and
its head necklaces are distinct. Give it weight \(|I|\). Complete
admissible rows are allowed as cyclic columns.

For \(2\le L\le p\), let

\[
 \Pi_L=\max\left\{
       \sum_{I\in\mathcal P}|I|:
       \mathcal P\text{ is split-shore-disjoint and }|I|\ge L
                        \right\}.                    \tag{3.1}
\]

### Theorem 3.1 (one matching and full-colouring lower bounds)

Every quotient perfect matching \(M\) satisfies

\[
                \boxed{r(M)\ge{T-\Pi_L\over L-1}.}   \tag{3.2}
\]

Every proper \(p\)-edge-colouring satisfies (0.5).

#### Proof

The maximal partial tagged runs of \(M\), together with its complete
tagged rows, form a split-shore-disjoint interval family: they are subsets
of one perfect matching. Delete all partial runs of length below \(L\).
There are \(r(M)\) of them and each loses at most \(L-1\) arcs. The
retained packing has weight at least

\[
                           T-(L-1)r(M).               \tag{3.3}
\]

It is feasible in (3.1), proving (3.2). Apply (3.2) to all \(p\) colour
matchings and use (1.4) to obtain (0.5). \(\square\)

Theorem 3.1 has the exact required scale. If (0.6) holds, then

\[
 S_{\rm tag}\ge
 {\delta pT\over\lceil CH\rceil-1}
 =\left({\delta\over C}+o(1)\right){pT\over H},        \tag{3.4}
\]

contradicting the desired little-oh. Conversely (0.2) and (3.3), with
\(L=\lceil CH\rceil\), give \(\Pi_L=T-o(T)\).

For the physical construction, the full one-factorization is stronger
than necessary. An extendable packing of weight \(T-u\), made of \(k\)
partial intervals of length at least \(L\), is sufficient for one exact
matching if

\[
            L/H\to\infty,\qquad k+u=o(T/H),           \tag{3.5}
\]

provided its residual split graph has a perfect matching. The prescribed
intervals contribute at most \(k\) runs, and the \(u\) completing edges
create at most \(u\) more. The residual Hall condition in this sentence
is essential: an arbitrary large interval packing need not extend.

## 4. Why the obvious owner-rounding proofs cannot settle (0.2)

### 4.1 The fractional interval optimum is exact

For a fixed row, a uniformly random coordinate relabelling makes its
cyclic order uniform. The simultaneous translation-rainbow count at the
middle rank gives

\[
 \Pr(\text{that row is nontransversal})
 \le {p^2(p-1)\over W}.                               \tag{4.1}
\]

There are \(T=W/p\) rows. Hence some relabelling leaves at most

\[
                             p(p-1)                  \tag{4.2}
\]

nontransversal rows.

On the remaining core, take all \(p\) cyclic exact length-\(L\) intervals
of every row. Every split resource has interval degree at most \(pL\),
and in the fully retained transversal system it has exact degree \(pL\).
Therefore

\[
                             x_I={1\over pL}          \tag{4.3}
\]

is a fractional matching. Its owner-weight objective is

\[
 \sum_I |I|x_I
 =(T-O(p^2))pL{1\over pL}=T-O(p^2).                  \tag{4.4}
\]

The left-shore capacity sum bounds every fractional objective by \(T\).
Thus the fractional optimum is asymptotically exact. In the ideal fully
transversal system it is exactly \(T\), with dual certificate
\(y_v=1/2\) on every split resource.

In the fully transversal system, for \(1\le L<p\), the paired resources
of one underlying necklace have

\[
 \boxed{d(O_L)=pL,\qquad d(O_L,O_R)=p(L-1).}          \tag{4.5}
\]

Indeed each of the \(p\) physical occurrences supplies \(L\) intervals
through one shore and \(L-1\) intervals containing both the incoming and
outgoing shore occurrences. The relative codegree is \(1-1/L\). This
is the desired continuity correlation, but it rules out a black-box
low-codegree nibble on the split hypergraph.

### 4.2 The natural spectral gap is always too small

Let \(P_0,P_1:\mathbb R^{pT}\to\mathbb R^T\) be the left- and right-fibre
sum maps and put

\[
                       K=\ker P_0\cap\ker P_1.        \tag{4.6}
\]

For a perfect matching indicator \(x\),

\[
 f=x-{1\over p}\mathbf1\in K,\qquad
 \|f\|_2^2=T\left(1-{1\over p}\right),               \tag{4.7}
\]

and (1.5) gives

\[
                        2r(M)=\|(I-U)f\|_2^2.        \tag{4.8}
\]

Define the relaxed gap

\[
 \gamma=\inf_{0\ne f\in K}
    {\|(I-U)f\|_2^2\over\|f\|_2^2}.                 \tag{4.9}
\]

The codimension of \(K\) is at most \(2T\). The real rowwise Fourier
space of frequencies \(0,\pm1\) has dimension \(3T\), so it meets \(K\)
in dimension at least \(T\). On that space,

\[
 \boxed{\gamma\le4\sin^2(\pi/p)\le{4\pi^2\over p^2}.}            \tag{4.10}
\]

A spectral lower bound strong enough to force \(r(M)\gg T/H\) would need
\(\gamma\gg1/H\). Equation (4.10) makes this impossible for \(H=o(p)\)
(indeed for \(H=o(p^2)\)). This closes the unweighted PSD/Poincare route;
it does not rule out an integral, nonquadratic obstruction.

### 4.3 Residue and complete-row Hall cuts are below scale

The Catalan congruence is

\[
                        T\equiv2(-1)^m\pmod p.        \tag{4.11}
\]

For each colour, complete monochromatic rows contribute multiples of
\(p\) selected tags, while the colour contains exactly \(T\) tags.
Therefore every colour has a partial run and

\[
                        S_{\rm tag}\ge p.             \tag{4.12}
\]

This is polynomial and negligible.

Let \(\nu\) be the matching number of the complete-row support
hypergraph. Each colour has at most \(\nu\) complete rows, so at most
\(p\nu\) rows are monochromatic across the whole colouring. Every other
cyclic row has at least two colour changes. Hence

\[
                  S_{\rm tag}\ge2(T-p\nu)_+.          \tag{4.13}
\]

Even the extreme \(\nu=0\) yields only \(2T=o(pT/H)\). Whole-row Hall and
the residue cannot decide the relaxed gate.

## 5. An abstract simple-row obstruction at scale \(W/\log p\)

This section proves (0.8). It is the reason an MSW-specific incidence
theorem is indispensable.

### Theorem 5.1 (random transversal quotient no-go)

Let \(p\to\infty\) and let \(T\) satisfy
\(p^3\log p+p^2\log T=o(pT)\); in particular
\(T=\operatorname {Cat}_m\), \(p=2m+1\), has this property. There is a
directed \(p\)-in/\(p\)-out quotient multigraph on \(T\) vertices whose
tagged arcs decompose into \(T\) directed simple \(p\)-cycles and for
which every proper \(p\)-edge-colouring has

\[
                        S_{\rm tag}>{pT\over3\log p}. \tag{5.1}
\]

#### Proof

Arrange \(W=pT\) labelled positions as \(T\) cyclic rows of length \(p\).
Choose a uniformly random labelled equipartition \(\mathcal P\) of these
positions into \(T\) blocks of size \(p\).

Fix a balanced position-colouring \(c\), meaning exactly \(T\) positions
of each of the \(p\) colours. A block is rainbow when it contains all
\(p\) colours. The exact probability that every block is rainbow is

\[
 P_0={ (T!)^p(p!)^T\over W!}
    =\exp(-(1+o(1))W),                               \tag{5.2}
\]

where the asymptotic follows directly from Stirling's formula and the
displayed growth assumption.

If a specified family of \(k\) blocks may be bad, every colour leaves
exactly \(k\) positions for those blocks. Counting injective assignments
to the good blocks and then partitioning the remaining \(pk\) positions
gives

\[
 \Pr(\text{all other blocks rainbow})
 \le
 \left({T!\over k!}\right)^p
 { (pk)!\over(p!)^k}{(p!)^T\over W!}.                 \tag{5.3}
\]

After choosing the exceptional blocks, the ratio to \(P_0\) is

\[
 R_k=\binom Tk{(pk)!\over(k!)^p(p!)^k}.               \tag{5.4}
\]

For \(K=2p^2\), elementary factorial bounds give

\[
 \log\sum_{k\le K}R_k
 =O(p^3\log p+p^2\log T)=o(W).                       \tag{5.5}
\]

Now count cyclic row-colourings with at most \(s\) switches. Choose one
initial colour per row, the switch positions, and the new colour after
each switch. This overcounts, and therefore gives the valid upper bound

\[
 N_s\le p^T\sum_{j\le s}\binom Wj(p-1)^j.            \tag{5.6}
\]

For

\[
                           s={W\over3\log p},         \tag{5.7}
\]

the logarithm of (5.6) is

\[
 \log N_s
 \le T\log p+s\log(eW/s)+s\log(p-1)
 ={W\over3}+o(W).                                    \tag{5.8}
\]

Equations (5.2), (5.5), and (5.8), followed by a union bound, show that
with probability \(1-o(1)\) no balanced colouring of switch cost at most
\(s\) is rainbow outside only \(2p^2\) blocks.

It remains to make every row transversal to the blocks. Let \(Z\) count
unordered same-row pairs lying in one block. Exactly

\[
 \mathbb EZ
 =T\binom p2{p-1\over W-1}< {p^2\over2}.             \tag{5.9}
\]

Thus there is a partition with the preceding anti-colouring property and
\(Z\le p^2\). Repair a repeated row in a block \(B\) as follows. Remove
one offending position \(x\) of row \(r\), and swap it with a position
\(y\) whose block contains no \(r\)-position and whose row is absent from
\(B\setminus\{x\}\). The first forbidden family contains at most \(p^2\)
positions and the second at most \(p^2\); since \(W>2p^2\), such a \(y\)
exists. The swap creates no new repeat and decreases \(Z\). At most
\(Z\) swaps repair all blocks, changing at most \(2p^2\) blocks. Call the
repaired transversal partition \(\mathcal P'\).

For a row position \((R,i)\), make its directed tagged arc go from the
\(\mathcal P'\)-block containing \((R,i)\) to the block containing
\((R,i+1)\). Row transversality makes every row a directed simple
\(p\)-cycle. Every block contains \(p\) positions, so the quotient has
indegree and outdegree \(p\). Its split graph is therefore \(p\)-regular
bipartite and is properly \(p\)-edge-colourable.

Any proper colouring is rainbow on every \(\mathcal P'\) tail block and
is globally balanced. On the original partition \(\mathcal P\), it is
rainbow outside the at most \(2p^2\) changed blocks. The anti-colouring
property therefore forces its row-switch cost above (5.7). This proves
(5.1). \(\square\)

If the final colours are encoded by
\(d=\lceil\log_2p\rceil\) binary splits, every colour switch changes at
least one bit. Hence the sum of binary row boundaries is at least
\(S_{\rm tag}\), and one split has

\[
             \Omega\left({W\over\log^2p}\right)      \tag{5.10}
\]

boundaries. This is much larger than \(T\). Therefore a universal
\(O(T)\)-per-level balanced \(b\)-factor lemma is false. Euler or Kempe
implementations cannot evade Theorem 5.1, because it bounds every proper
colouring of the constructed system.

The theorem has exact negative scope: it is not an MSW-voltage
realization. It closes only arguments using regularity, simple rows, and
generic recolouring machinery.

## 6. Missing shadows: exact ledger and a mixed-run Hall cut

Fix one colour matching \(M\). At depth \(q\), the lower target-necklace
universe and its complementary upper typed copy both have size

\[
 K_q={1\over p}\binom p{m-q}=T\rho_q.                \tag{6.1}
\]

Let \(\mathcal R_q^\pm(M)\) be the target necklaces supplied by windows
lying wholly in a tagged run or complete tagged row. Put

\[
 D^{\rm inh}_{\le Q}(M)
 =\sum_{q=1}^Q\sum_{\epsilon\in\{-,+\}}
       \left(K_q-|\mathcal R_q^\epsilon(M)|\right).   \tag{6.2}
\]

### Lemma 6.1 (open-run capacity)

For an open tagged run of length \(\ell\), the total number of inherited
starts of one sign through depths \(1,\ldots,Q\) is at most

\[
 h_Q(\ell)=\sum_{q=1}^Q(\ell-2q+1)_+.                \tag{6.3}
\]

If \(\ell\le L_0\) and \(Q\le L_0/2\), then

\[
            \boxed{h_Q(\ell)\le
            \ell\left(Q-{Q^2\over L_0}\right).}     \tag{6.4}
\]

#### Proof

If \(\ell\ge2Q-1\), then \(h_Q(\ell)=Q\ell-Q^2\), and (6.4) follows from
\(\ell\le L_0\). If \(\ell<2Q-1\), the positive terms in (6.3) form a
quadratic cap and \(h_Q(\ell)\le\ell^2/4\). Hence

\[
 {h_Q(\ell)\over\ell}\le{\ell\over4}<{Q\over2}
 \le Q-{Q^2\over L_0},                               \tag{6.5}
\]

using \(Q\le L_0/2\). \(\square\)

### Theorem 6.2 (mixed-run direct-shadow obstruction)

Let \(R_{\le L_0}(M)\) be the number of selected quotient arcs belonging
to partial tagged runs of length at most \(L_0\). Then (0.10) holds.

#### Proof

Apply Lemma 6.1 to every short partial run and grant every remaining
selected arc—the arcs in longer partial runs and complete cyclic
rows—the maximal possible one target per sign at every depth. The total
two-sign inherited support is at most

\[
 \begin{aligned}
 &2R_{\le L_0}\left(Q-{Q^2\over L_0}\right)
   +2Q(T-R_{\le L_0})\\
 &\hspace{35mm}=2QT-{2Q^2\over L_0}R_{\le L_0}.       \tag{6.6}
 \end{aligned}
\]

The typed target universe has cardinality

\[
                2T\sum_{q=1}^Q\rho_q
 =2QT-2T\sum_{q=1}^Q(1-\rho_q).                      \tag{6.7}
\]

Support cannot exceed occurrence count. Subtract (6.6) from (6.7) and
truncate at zero. \(\square\)

The product in (0.9) gives the elementary exact estimate

\[
 \begin{aligned}
 1-\rho_q
 &\le\sum_{j=0}^{q-1}{2(j+1)\over m+2+j}
 \le {q(q+1)\over m},\\
 \sum_{q=1}^Q(1-\rho_q)
 &\le {Q(Q+1)(Q+2)\over3m}.                           \tag{6.8}
 \end{aligned}
\]

Now suppose \(H\ge c_0\sqrt m\), \(L_0\to\infty\), and
\(L_0=O(m^{2/3})\). For an arbitrary fixed \(c>0\), take

\[
                        Q=\lfloor c\sqrt{L_0}\rfloor.             \tag{6.9}
\]

Then \(Q\le H\) and \(Q\le L_0/2\) eventually. If the left side of
(0.10) is \(o(T)\), equations (0.10) and (6.8) imply

\[
 {R_{\le L_0}\over T}
 \le\left({c\over3}+o(1)\right){L_0^{3/2}\over m}.    \tag{6.10}
\]

For \(L_0=O(m^{2/3})\), first let \(m\to\infty\) and then let the fixed
\(c\downarrow0\). This proves (0.11).

For comparison, in a pure exact-length open catalogue, assume
\[
 Q=\lfloor m/L\rfloor\to\infty,\qquad
 Q\le H,\qquad Q\le(L+1)/2.                           \tag{6.10a}
\]
For example, \(\sqrt{2m}\le L=o(m)\) and \(m/L\le H\) suffice.
Taking this \(Q\) gives the explicit asymptotic deficit

\[
 D^{\rm inh}_{\le Q}
 \ge\left({4\over3}-o(1)\right)T{m^2\over L^3}.       \tag{6.11}
\]

Thus direct open-interval support cannot have \(o(T)\) aggregate holes at
\(L=O(m^{2/3})\) within (6.10a). This pure statement excludes complete
rows, longer runs, extra root-cocycle continuations, and external collar
homes. The mixed theorem (0.10) records the first two escape columns; the
last two lie outside the inherited-run support being counted.

### Exact seam/support sandwich

Let \(\mathcal A_q^\pm(M)\) be the actual target support of the selected
factor at depth \(q\), including seam-crossing starts, and let

\[
                      h_q^\pm=K_q-|\mathcal A_q^\pm|.             \tag{6.12}
\]

There are at most \((2q-1)r(M)\) quotient start orbits crossing declared
tag cuts. Hence

\[
 \boxed{
 \left(K_q-|\mathcal R_q^\pm|-(2q-1)r(M)\right)_+
 \le h_q^\pm
 \le K_q-|\mathcal R_q^\pm|.}                       \tag{6.13}
\]

Summing the possible improvement supplied by seam-crossing starts gives
\(H^2r(M)\) per sign. Therefore \(r=o(T/H)\) alone controls each fixed
depth to \(o(T)\), but the raw all-depth ambiguity is only \(o(TH)\), not
\(o(T)\). A common collar may reuse one boundary neighbourhood across all
depths, but its actual target support must be proved; it is not a
consequence of the run count.

At a fixed depth, if the inherited or collared occurrence loads are
\(\mu_q(T)\), put

\[
 G_q=\sum_T\mu_q(T),\qquad
 R_q=\sum_T(\mu_q(T)-1)_+,\qquad
 D_q=K_q-|\{T:\mu_q(T)>0\}|.                         \tag{6.14}
\]

Then the exact missing/repeat identity is

\[
                        \boxed{D_q=R_q-(G_q-K_q).}   \tag{6.15}
\]

Thus low switching controls neither the repeat excess nor the support
union.

A clean one-colour sufficient interface is

\[
 \boxed{
 Hr(M)+D^-(M)=o(T),}                                  \tag{6.16}
\]

where \(D^-(M)\) is the aggregate quotient lower-shadow deficiency after
the chosen common collar assignment. Translation lifting multiplies
both terms by \(p\). For a full colouring, the averaging version is

\[
 H S_{\rm tag}(\chi)+\sum_aD_a^-=o(pT),               \tag{6.17}
\]

which supplies a colour satisfying (6.16). The switch hypothesis gives
only the first term of (6.17).

## 7. Certified boundary

### Proved

1. The exact tagged run identities (1.4)–(1.5).
2. The \(p=5\) root-hopping counterexample and exact repair cocycle
   (1.12), showing that static one-step orbit activity does not by itself
   certify an \(H\)-long original-row segment.
3. The long-segment extraction theorem at the relaxed scale, with the
   physical cut, component, and collar ledgers (2.6)–(2.12).
4. The exact one-matching and full-colouring interval obstruction
   (3.2) and (0.5).
5. Exact fractional owner saturation, the paired-shore codegree
   (4.5), and the spectral no-go (4.10).
6. The abstract simple-row obstruction \(S_{\rm tag}>W/(3\log p)\), which
   rules out every proof based only on regularity, row transversality, or
   generic recolouring.
7. The mixed-run direct-shadow inequality (0.10), its \(m^{2/3}\)
   consequence (0.11), the seam/support sandwich (6.13), and the exact
   repeat identity (6.15).

### Not proved

1. A proper colouring of the actual projected MSW graph satisfying
   \(S_{\rm tag}=o(pT/H)\).
2. An actual-MSW estimate \(\Pi_{CH}\le(1-\delta)T\) refuting that
   colouring theorem.
3. An extendable almost-spanning MSW interval packing; the fractional
   packing does not settle its growing-rank integrality.
4. The \(H\)-overlap cocycle with few stateful failures for an
   orbit-aware matching.
5. Aggregate \(o(T)\) quotient shadow deficiency for the same colour.
6. Coefficient one.

The exact surviving gate is now narrow. One must exploit a genuine
Dyck/MSW incidence property to construct an extendable matching whose
mass is concentrated in super-\(H\), and for direct inherited support
essentially super-\(m^{2/3}\), rooted segments, or else build a literal
common collar which supplies the missing target unions. None of these
requirements follows from König edge-colouring or from the relaxed switch
scale alone.
