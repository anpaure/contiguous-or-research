# Cluster superedges cannot remove the domino-twin first-shadow excess

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver,
probabilistic black box, or web input is used.

## 0. Verdict

Put

\[
 n=2m,\qquad R=m-q_0=2r+1,
 \qquad q_0=A\sqrt m+O(1),
\tag{0.1}
\]

and let

\[
                         N=\binom nR=\Theta(W).
\tag{0.2}
\]

A simple domino-twin entrance atom is an unoriented cyclic necklace of
unordered dominoes

\[
                         B_0,B_1,\ldots,B_{m-1}.
\tag{0.3}
\]

It has \(2n\) entrance targets and admits \(2^{m-1}\) decompositions
into two entrance-disjoint ordinary cyclic packets.  One may place
arbitrary collections of such lifted atoms into clusters and, after the
clusters have been selected, choose their internal atoms and their
component decompositions in an arbitrary correlated way.

The cluster freedom does not repair the first shadow.

### Theorem A (cluster-independent first-shadow cut)

Suppose \(s\) selected cluster superedges are instantiated by lifted
domino-twin atoms

\[
                  \widehat Q_i=(Q_i;P_i,P_i'),
                  \qquad 1\le i\le s,
\tag{0.4}
\]

whose underlying entrance supports \(Q_i\) are pairwise disjoint.  No
condition is imposed on the clusters, on the rule choosing
\(\widehat Q_i\), or on correlations among the choices.  At the lower
first shadow, of interval length \(R-1\), the \(2s\) ordinary component
packets have support size at most

\[
                         {3n\over2}s,
\tag{0.5}
\]

and raw repeat excess at least

\[
                         {n\over2}s=ms.
\tag{0.6}
\]

If the selected superedges form an entrance near-factor, so that

\[
                         2ns=N-o(N),
\tag{0.7}
\]

then the floor-correct first-shadow excess satisfies

\[
 \boxed{
 \widetilde E_{q_0+1}
 \ge \left({1\over4}-o(1)\right)N
 =\Theta(W).}
\tag{0.8}
\]

The same conclusion holds at the complementary upper first shadow.
Thus an entrance near-factor of cluster superedges is not useful for the
constant-one compiler.

### Theorem B (convexification does not help)

For every probability distribution, fractional point, or dependent
rounding rule which chooses one lifted member of each chosen cluster,
the expected first-shadow support contributed per unit cluster mass is
at most \(3n/2\).  Hence the fractional descendant-support program has
the same deficit

\[
 \sum_T z_T\le {3n\over2}\sum_C x_C.
\tag{0.9}
\]

Replacing a cluster by the coordinatewise union of the shadows of all
its members can violate (0.9), but that union is not a realizable
superedge: it uses different internal representatives for different
targets.

### Theorem C (no internal rebundling)

Fix one simple entrance atom \(Q\).  If two ordinary component packets
inside \(Q\) are entrance-disjoint and together give exact Boolean
ownership of \(Q\), then they are a complementary pair.  Every such pair
has exactly \(m\) common lower first-shadow targets.  Therefore no
choice of a different internal orientation, no paired-corridor
repartition, and no recombination of two components while staying
inside one \(Q\) changes (0.6).

The only structural escape is to dissolve the twin atom and select
ordinary cyclic packets globally, forbidding simultaneous selection of
complementary twin traces.  The capacity-one twin-fibre labels from the
ordinary-packet formulation implement precisely that exclusion, but
they do not by themselves construct the required ordinary-packet
matching.  This is a different rounding problem, not a
cluster-superedge repair.

## 1. Exact internal geometry of one atom

Choose an orientation

\[
 v=(v_0,\ldots,v_{m-1})\in\{0,1\}^m
\tag{1.1}
\]

of the dominoes.  Write

\[
 f_i(v)=b_i^{v_i},\qquad s_i(v)=b_i^{1-v_i},
\tag{1.2}
\]

and let \(P_v\) be the cyclic word

\[
 f_0(v),s_0(v),f_1(v),s_1(v),\ldots,
 f_{m-1}(v),s_{m-1}(v).
\tag{1.3}
\]

At entrance length \(R=2r+1\), put

\[
                         C_i=B_i\cup\cdots\cup B_{i+r-1}.
\tag{1.4}
\]

The simple atom is

\[
 Q=\{C_i\cup\{z\}:
      i\in\mathbb Z_m,
      z\in B_{i-1}\cup B_{i+r}\}.
\tag{1.5}
\]

Over the core \(C_i\), the ordinary component \(P_v\) contains the two
entrance targets

\[
 C_i\cup\{f_{i+r}(v)\},
 \qquad
 C_i\cup\{s_{i-1}(v)\}.
\tag{1.6}
\]

For two orientations \(v,w\), targets with different core indices
cannot coincide, while at a fixed core the two displayed targets agree
exactly when the corresponding orientation bits agree.  Consequently

\[
 |P_R(P_v)\cap P_R(P_w)|
       =2|\{i:v_i=w_i\}|.
\tag{1.7}
\]

In particular,

\[
 P_R(P_v)\cap P_R(P_w)=\varnothing
              \quad\Longleftrightarrow\quad w=\bar v.
\tag{1.8}
\]

Thus exact Boolean ownership of \(Q\) forces the complementary
decomposition \(\{P_v,P_{\bar v}\}\).  There is no second internal
pairing of the two component slots which preserves the entrance owner
set.

Now pass to the first shadow.  Its interval length is

\[
                         R-1=2r.
\tag{1.9}
\]

For every \(i\in\mathbb Z_m\), the interval beginning at the first
position of \(B_i\) is the whole-domino target

\[
                         D_i=B_i\cup\cdots\cup B_{i+r-1}.
\tag{1.10}
\]

It is independent of \(v\), so \(D_i\) lies in both first-shadow decks
of \(P_v\) and \(P_{\bar v}\).  These \(m\) targets are distinct.

Every other length-\(2r\) interval has exactly one selected member from
each of two boundary dominoes and all intervening dominoes whole.  Its
counterpart under \(v\mapsto\bar v\) selects the opposite member at
both boundaries.  Since \(2\le r\le m-2\) in the Gaussian range, the
whole internal dominoes recover the two boundary blocks, so the two
targets are distinct.  Such a split-boundary target cannot equal a
whole-domino target.  Hence

\[
 |P_{R-1}(P_v)\cap P_{R-1}(P_{\bar v})|=m={n\over2},
\tag{1.11}
\]

and therefore

\[
 |P_{R-1}(P_v)\cup P_{R-1}(P_{\bar v})|
 =2n-m={3n\over2}.
\tag{1.12}
\]

Equations (1.11)--(1.12) are statewise.  Changing the necklace by a
paired-corridor move changes the literal sets \(D_i\), but never their
number or their double occurrence.

## 2. Proof of the cluster cut

For a selected lift \(\widehat Q_i\), let

\[
 \mu_i(T)\in\{0,1,2\}
\tag{2.1}
\]

be the number of its two component first-shadow decks containing \(T\).
By (1.11), exactly \(m\) targets have \(\mu_i(T)=2\).  Put

\[
                         \mu(T)=\sum_{i=1}^s\mu_i(T).
\tag{2.2}
\]

There are \(2ns\) total first-shadow occurrences.  From (1.12),

\[
 |\{T:\mu(T)>0\}|
 \le\sum_{i=1}^s|\{T:\mu_i(T)>0\}|
 ={3n\over2}s.
\tag{2.3}
\]

Thus

\[
 \sum_T(\mu(T)-1)_+
 =2ns-|\{T:\mu(T)>0\}|
 \ge {n\over2}s,
\tag{2.4}
\]

proving (0.5)--(0.6).  Notice that collisions between different atoms
can only decrease the union in (2.3), so cross-cluster correlation can
only increase this lower bound.

Let \(M=2ns\) and

\[
                         N_1=\binom n{R-1}.
\tag{2.5}
\]

The floor-correct excess is

\[
 \widetilde E_{q_0+1}
 =\min\{M,N_1\}-|\{T:\mu(T)>0\}|.
\tag{2.6}
\]

Since

\[
 {N_1\over N}
 ={R\over n-R+1}
 =1-O(m^{-1/2}),
\tag{2.7}
\]

conditions (0.7), (2.3), and (2.6) yield

\[
 \widetilde E_{q_0+1}
 \ge \min\{N-o(N),N-o(N)\}
       -{3\over4}(N-o(N))
 =\left({1\over4}-o(1)\right)N.
\tag{2.8}
\]

Complementation takes the common lower first-shadow targets to common
upper first-shadow targets and preserves all multiplicities.  This
proves the upper assertion and Theorem A.

## 3. Fractional and randomized internal choices

Let \(\mathcal C\) be an arbitrary cluster family.  For each cluster
\(C\in\mathcal C\), let \(\mathcal A(C)\) be its permitted lifted
internal atoms.  A fractional internal choice consists of numbers

\[
                         y_{C,a}\ge0,
 \qquad a\in\mathcal A(C),
 \qquad \sum_{a\in\mathcal A(C)}y_{C,a}=x_C.
\tag{3.1}
\]

For every realizable descendant-support variable \(z_T\),

\[
 z_T\le
 \sum_C\sum_{a\in\mathcal A(C)}
 y_{C,a}\mathbf1_{\{T\in\operatorname {supp}_1(a)\}}.
\tag{3.2}
\]

Sum over \(T\), apply (1.12) to every \(a\), and use (3.1):

\[
 \sum_Tz_T
 \le {3n\over2}\sum_C\sum_a y_{C,a}
 ={3n\over2}\sum_Cx_C.
\tag{3.3}
\]

This proves Theorem B.  Dependence among integral choices is irrelevant:
(1.12) holds for every outcome before expectation is taken.

The tempting replacement

\[
 \operatorname {supp}_1(C)
 :=\bigcup_{a\in\mathcal A(C)}
              \operatorname {supp}_1(a)
\tag{3.4}
\]

does not define a literal packet.  A target in the union may require
orientation \(v\), while another requires an incompatible orientation
\(w\).  Counting both spends the cluster mass once but uses two internal
states.  Formula (3.3) is the exact correction.

## 4. Why cross-pairing does not constitute an internal repair

Merely changing the bookkeeping pairing of already selected ordinary
components does not change their first-shadow multiset.  In particular,
if both \(P_v\) and \(P_{\bar v}\) remain selected, pairing either with
components from other clusters leaves the \(m\) common targets in
(1.11) present twice.

To remove this charge one must omit at least one member of almost every
complementary pair.  Doing so destroys exact ownership of its \(2n\)-set
\(Q\): one retained component owns only \(n\) of those entrance targets.
The missing ownership must then be supplied by different ordinary
packets.  This is precisely a global matching in the ordinary cyclic
packet catalogue, not a choice of a representative of the original
cluster superedge.

There is an exact local exclusion mechanism for that different problem.
Every ordinary packet \(P\) lies in two simple domino-twin fibres,
corresponding to the two alternating perfect matchings of its cyclic
positions.  Attach those two fibre labels to \(P\), each with capacity
one.  Then no complementary twin pair can be selected.  This removes
the statewise charge (1.11), while adding only two resources to each
ordinary packet.  It does not prove that the augmented ordinary
catalogue has a critical integral matching with \(o(W)\) all-depth
defect.

Accordingly there is no explicit rebundling construction inside the
cluster-superedge model.  The literal twin lane is closed at the
fractional support level, before cluster matching, thinning, or stopped
regeneration enter.

## 5. Exact surviving gate

The cluster-thinning programme should be retired for the twin
catalogue.  Its overlap estimates concern whether entrance superedges
can be packed; Theorems A--B show that even a perfect entrance packing
has the wrong descendant support.

The surviving problem is the ordinary-packet mixed-depth rounding gate:
select entrance-disjoint ordinary cyclic packets, impose capacity one
on the two twin-fibre labels of every packet, and achieve

\[
                 \sum_{q\le H}\widetilde E_q=o(W).
\tag{5.1}
\]

No cluster quotient of intact twin atoms can imply (5.1).
