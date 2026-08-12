# BTK expiration collars have a linear physical-mass toll

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

Let

\[
 H=\left\lfloor\sqrt m\,\omega\right\rfloor,
 \qquad \omega=\log\log m,
 \qquad W=\binom{2m}{m}.
\tag{0.1}
\]

Use the standard BTK SCD on each of two \(m\)-coordinate halves and its
rank-\(m\) product diagonals.  An intact diagonal of length \(h\) means
that its complete standard Johnson word occurs consecutively, in either
orientation, in the routed factor.

The coherent-sink obstruction cannot be repaired by sublinear physical
expiration collars.

### Theorem 0.1 (motion-or-expiration bound)

Let an intact BTK product diagonal \(P\) of length

\[
                         5\le h\le H/3
\tag{0.2}
\]

be followed in a route by another intact BTK product diagonal \(Q\).
Let \(t\) be the number of Johnson edges in the connector from the last
owner of \(P\) to the first owner of \(Q\).  If the complete word is
two-sided \(H\)-safe, then

\[
                         \boxed{t\ge\lceil h/4\rceil.}
\tag{0.3}
\]

This includes every shared collar: \(t\) counts each physical connector
edge once, regardless of how many earlier queues it is claimed to flush.

### Theorem 0.2 (global collar/surgery min--max)

Consider an owner-disjoint route cover with \(p\) components.  Relative
to the original BTK product partition, let

\[
 M=\sum_{\substack{P:\ 5\le h(P)\le H/3\\
                    P\text{ is not traversed intact}}}h(P)
\tag{0.4}
\]

be the baseline edge mass of the short atoms touched by surgery.  Order
the intact short atoms along every routed component, and let \(T\) be
the sum of the connector lengths between consecutive such atoms.  These
connector intervals are disjoint along the routed components.  Then

\[
 \boxed{
 M+4T+\frac H3p\ge W-o(W).}
\tag{0.5}
\]

In particular, under the required component bound \(p=o(W/H)\),

\[
                         \boxed{M+4T\ge W-o(W).}
\tag{0.6}
\]

Therefore:

1. if the BTK atoms remain intact, then \(T\ge(1/4-o(1))W\);
2. if the total literal collar length is \(T=o(W)\), then
   \(M\ge W-o(W)\);
3. even charging the combined physical cost \(C=M+T\), one has

   \[
                         C\ge(1/4-o(1))W.
\tag{0.7}
   \]

Thus private collars, shared collars, and close packing cannot give a
sublinear **physical-mass** repair.  The only surviving possibility is a
global refactorization which changes atoms containing \(W-o(W)\) baseline
edge incidences and proves a separate cancellation theorem for their flag
profiles.

The theorem deliberately does not claim that the number of splice arcs is
linear.  Cutting one edge in each of
\(\Theta(W/\sqrt m)\) typical atoms uses only \(o(W)\) splice arcs while
touching \(\Theta(W)\) owner mass.  Hence a bounded-splice but
full-mass telescoping construction is not excluded; it is no longer an
expiration-collar repair in the sublinear-mass sense.

## 1. Exact BTK record-tail Lipschitz law along a connector

For a middle owner \(X\), write \(w_X\) for its \(A\)-restriction.  If
\(|w_X|=(m+h_X)/2>m/2\), define \(I(X)\) to be the terminal
\(h_X\)-set of strict ascending record times of the BTK prefix walk.
At a high endpoint of a product diagonal \(P\),

\[
                         I(X)=I_A(P).
\tag{1.1}
\]

The record-tail audit in
MATH_OBSTRUCTION_BTK_PRODUCT_SCD_ENDPOINT_RECORD_TAIL_CUT_20260726.md
proves the following one-edge statement.  If \(X,X'\) are Johnson
neighbors whose \(A\)-ranks are above \(m/2\), then

\[
                         |I(X)\setminus I(X')|\le4.
\tag{1.2}
\]

Indeed, an internal \(A\)-exchange changes the full record set in at
most four places, a cross-half edge changes it in at most two places and
changes the prescribed tail length by two, and an internal \(B\)-edge
does not change it.

### Lemma 1.1 (connector survival)

Let

\[
                         X=X_0,X_1,\ldots,X_t=Y
\tag{1.3}
\]

be a Johnson connector starting at a high endpoint \(X\) of length
\(h\).  If \(t<h/4\), then every \(X_s\) has \(A\)-rank above \(m/2\),
the endpoint \(Y\) is high whenever it is a product endpoint, and

\[
 h(Y)\in[h-2t,h+2t],
\qquad
 |I(X)\cap I(Y)|\ge h-4t>0.
\tag{1.4}
\]

#### Proof

The excess of the \(A\)-rank over \(m/2\) starts at \(h/2\) and changes
by at most one on each Johnson edge.  Thus it remains at least
\(h/2-t>h/4>0\).  At the endpoint this gives
\(|h(Y)-h|\le2t\) and forces the high sign.

Iterating (1.2) gives

\[
 |I(X)\setminus I(Y)|
 \le\sum_{s=0}^{t-1}|I(X_s)\setminus I(X_{s+1})|
 \le4t.
\]

Since \(|I(X)|=h\), (1.4) follows. \(\square\)

The low-end version follows by reverse-complement and the half swap,
with the same physical-label conclusion.

## 2. Proof of the connector lower bound

Traverse \(P\), then the \(t\)-edge connector, then \(Q\).  Suppose for
contradiction that

\[
                         t<h/4.
\tag{2.1}
\]

By Lemma 1.1, the starting endpoint of \(Q\) has the same sign as the
ending endpoint of \(P\),

\[
                         h(Q)<\frac32h,
\tag{2.2}
\]

and the two intact words have a common physical active label \(c\).

Number the complete edge word from the first edge of \(P\).  The
occurrence of \(c\) in \(P\) has some position

\[
                         1\le i\le h,
\]

while its occurrence in \(Q\) has some position

\[
                         h+t+1\le j\le h+t+h(Q).
\]

Consequently

\[
\begin{aligned}
 j-i
 &\le h+t+h(Q)-1\\
 &<h+\frac h4+\frac{3h}{2}
 =\frac{11h}{4}
 \le\frac{11H}{12}
 <H.
\end{aligned}
\tag{2.3}
\]

The two occurrences therefore belong to one \(H\)-edge window,
contradicting two-sided \(H\)-safety.  Hence \(t\ge h/4\); integrality
gives (0.3).  The low-end case is the complemented argument.
\(\square\)

Notice the dichotomy behind the proof.  A connector must either move at
least \(h/4\) Johnson steps, so that the BTK record tail can be replaced,
or be long enough for the old occurrence to expire.  In the range
\(h\le H/3\), both alternatives cost at least \(h/4\).

## 3. Almost all baseline edge mass is in the short range

Put

\[
                         c_m=\binom m{\lfloor m/2\rfloor}.
\tag{3.1}
\]

The product partition contains \(c_m^2\) paths.  If \(P_h\) denotes the
number of paths of length \(h\), then, with \(r=(m-h)/2\),

\[
 P_h=\binom mr^2-\binom m{r-1}^2,
\tag{3.2}
\]

and the middle-owner partition gives

\[
 \sum_h(h+1)P_h=W.
\tag{3.3}
\]

Therefore the total baseline edge mass is

\[
                         \sum_hhP_h=W-c_m^2=W-o(W).
\tag{3.4}
\]

We need the stronger fact that the part with \(h>H/3\) is \(o(W)\).
For an admissible threshold \(L\), put

\[
 r_L=\left\lfloor\frac{m-L}{2}\right\rfloor,
 \qquad B_r=\binom mr^2.
\]

Summation by parts in (3.2) gives the exact tail-owner identity

\[
 \sum_{h\ge L}(h+1)P_h
 =(m-2r_L+1)B_{r_L}
   +2\sum_{r=0}^{r_L-1}B_r.
\tag{3.5}
\]

For \(r\le r_L\),

\[
 \frac{B_{r-1}}{B_r}
 =\left(\frac r{m-r+1}\right)^2
 \le
 \left(\frac{r_L}{m-r_L+1}\right)^2.
\tag{3.6}
\]

The geometric sum in (3.5), together with the exact central-binomial
ratio, yields

\[
 \sum_{h\ge L}(h+1)P_h
 \le
 C\left(\frac L{\sqrt m}+\frac{\sqrt m}L\right)
   \exp\left[-\frac{L^2-O(L)}m\right]W
\tag{3.7}
\]

for an absolute constant \(C\), uniformly when
\(\sqrt m\ll L=o(m)\).

Take \(L=H/3+O(1)\).  Then (3.7) is

\[
 O\left(
   \left(\omega+\omega^{-1}\right)
   e^{-\omega^2/9+o(\omega^2)}W\right)
 =o(W).
\tag{3.8}
\]

The finitely many lengths \(h<5\) contribute \(o(W)\).  Combining this
with (3.4) proves

\[
 \boxed{
 \sum_{5\le h\le H/3}hP_h=W-o(W).}
\tag{3.9}
\]

## 4. Global disjoint-gap ledger

Let \(\mathcal I\) be the intact baseline atoms with
\(5\le h\le H/3\), and let \(\mathcal M\) be the non-intact atoms in the
same range.  Thus

\[
 \sum_{P\in\mathcal M}h(P)=M.
\tag{4.1}
\]

In each routed component, list the members of \(\mathcal I\) in their
order of occurrence.  Between two consecutive listed atoms lies one
connector interval.  Distinct such intervals are edge-disjoint, even if
the construction calls them shared collars or fills them with pieces of
other atoms.

Theorem 0.1 gives

\[
                         4T
 \ge\sum_{\substack{P\in\mathcal I\\
                    P\text{ is not last in its component}}}h(P).
\tag{4.2}
\]

At most \(p\) intact short atoms are last among the intact short atoms of
their components, and each has length at most \(H/3\).  Hence, by (3.9),

\[
\begin{aligned}
 4T
 &\ge
 \sum_{5\le h\le H/3}hP_h-M-\frac H3p\\
 &=W-o(W)-M-\frac H3p.
\end{aligned}
\tag{4.3}
\]

Rearrangement proves (0.5), and \(p=o(W/H)\) proves (0.6).
Finally,

\[
 4(M+T)\ge M+4T\ge W-o(W)
\]

proves (0.7).

The same ledger holds for cycle components: there is then no terminal
subtraction on that cycle.

## 5. What is and is not closed

Closed:

* independent \(H\)-edge flushes at product endpoints;
* any claimed sharing which still uses literal connector edges in an
  owner-disjoint path/cycle cover;
* close packing which leaves all but \(o(W)\) baseline edge mass inside
  intact BTK atoms; and
* every hybrid with \(M=o(W)\), \(T=o(W)\), and \(p=o(W/H)\).

Not closed:

* cutting \(o(W)\) arcs but thereby refactoring atoms containing
  \(\Theta(W)\) owner mass;
* a global interleaving whose changed flag contributions telescope even
  though almost every owner lies in a touched atom; or
* changing to a genuinely different SCD/frame family with non-Lipschitz
  endpoint alphabets.

Thus an expiration collar is not a sublinear repair of the coherent BTK
sinks.  Any surviving close-packed construction must be a full-mass
global factorization, with a new exact flag-cancellation theorem; local
collar sharing cannot supply it.
