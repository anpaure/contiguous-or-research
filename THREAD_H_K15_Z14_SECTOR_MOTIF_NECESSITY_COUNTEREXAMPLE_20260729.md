# The \(z_{14}\) sector atlas does not localize compiler-Hall descent

Date: 2026-07-29

Status: proved the exact \(z_{14}\) sector census, proved the strongest
support-level duplicate-repair statement, and gave a certified physical
counterexample to the stronger claim that every occurrence-labelled
compiler-Hall-improving switch repairs one of the bounded sector defects.
The counterexample is non-equivariant; it does not exclude a theorem using
essential strict \(C_{15}\) orbit closure. Both endpoints retain four
\(q=1\) holes and three doubles, so it is also not a counterexample under
an additional hypothesis of global \(q=1\) injectivity. It refutes the
stepwise necessity claim for the actual H19 descent lane.

## 1. Definitions

Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad W=\binom{15}{8}=6435,
\]

be a Johnson path enumerating every rank-eight mask exactly once. For an
edge \(e_i=T_iT_{i+1}\), write

\[
 \lambda_i=T_i\cap T_{i+1},\qquad
 \upsilon_i=T_i\cup T_{i+1}.
\tag{1.1}
\]

Thus \(|\lambda_i|=7\) and \(|\upsilon_i|=9\). Fix

\[
 z=14,\qquad Z=2^{14}.
\]

Call a middle vertex \(A\) if it contains \(z\), and \(B\) otherwise.
Edges have types \(AA,BB\), or \(X\), where \(X\) is a cross edge.

For a rank-seven mask \(Q\), put

\[
 d_T(Q)=|\{i:\lambda_i=Q\}|.
\tag{1.2}
\]

The \(q=1\) hole count and repeat excess are

\[
 h_1(T)=|\{Q:d_T(Q)=0\}|,\qquad
 e_1(T)=\sum_Q(d_T(Q)-1)_+.
\tag{1.3}
\]

## 2. Exact sector classification

### Lemma 2.1 (clique model and path deficit)

For every rank-seven \(Q\), let

\[
 K_Q=\{Q\cup\{x\}:x\notin Q\}.
\tag{2.1}
\]

Then \(K_Q\) is an eight-vertex clique in \(J(15,8)\), and \(d_T(Q)\)
is exactly the number of carrier edges induced by \(K_Q\). Moreover,

\[
 \boxed{h_1(T)=e_1(T)+1.}
\tag{2.2}
\]

If \(z\in Q\), every occurrence of \(Q\) is \(AA\). If \(z\notin Q\),
\(K_Q\) has one \(A\)-vertex, namely \(Q\cup\{z\}\), and seven
\(B\)-vertices. Consequently a multiplicity-two \(z\)-free label has
sector type

\[
 BB/BB,\qquad BB/X,\qquad\text{or}\qquad X/X.
\tag{2.3}
\]

#### Proof

Two distinct members \(Q\cup\{x\},Q\cup\{y\}\) intersect in \(Q\) and
differ by one exchange. Conversely, every rank-eight Johnson edge with
intersection \(Q\) has this form. This proves the clique assertion.

There are \(6435\) possible rank-seven labels and \(6434\) path edges.
Writing \(s=6435-h_1(T)\) for the support size, occurrence counting gives

\[
 6434=s+e_1(T)=6435-h_1(T)+e_1(T),
\]

which is (2.2).

If \(z\in Q\), all eight supersets contain \(z\). If \(z\notin Q\),
only the supermask obtained by adding \(z\) contains it. This proves the
sector assertions. \(\square\)

### Theorem 2.2 (the authoritative H19 \(z_{14}\) atlas)

For the authoritative H19 carrier

    scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json

whose middle-path SHA-256 is

    97429bb3f25ccf921e794c1d20ed361684116823d0a14787634dc22af820e441,

the sector counts are

\[
 AA=3004,\qquad AB=428,\qquad BA=428,\qquad BB=2574.
\tag{2.4}
\]

The only repeated lower labels are

\[
\begin{array}{c|c|c|c}
\text{label}&\text{edge positions}&\text{sector}&\text{physical edges}\\ \hline
17140&2582,5917&AA/AA&
17142\!-\!21236,\ 17148\!-\!17396\\
12685&840,5046&BB/BB&
14733\!-\!13197,\ 13709\!-\!12687\\
3868&2553,5549&BB/X&
3900\!-\!3996,\ 3869\!-\!20252.
\end{array}
\tag{2.5}
\]

The holes are exactly

\[
 H=\{5801,7267,8877,13620\}.
\tag{2.6}
\]

All four holes omit \(z\). In particular, the \(3003\) \(z\)-containing
rank-seven labels are all covered by the \(3004\) \(AA\) edges, with
\(17140\) the sole repeated one.

#### Proof

The literal edge table gives (2.5)--(2.6). Lemma 2.1 then gives repeat
excess three from four holes, so the table is exhaustive.

There are \(\binom{14}{7}=3432\) \(A\)-vertices and
\(\binom{14}{8}=3003\) \(B\)-vertices. Both path endpoints are \(B\).
The \(856\) cross edges therefore form \(428\) entrances and \(428\)
exits of \(A\)-runs. Hence there are \(428\) \(A\)-runs and \(429\)
\(B\)-runs, giving

\[
 AA=3432-428=3004,\qquad
 BB=3003-429=2574.
\]

This proves (2.4). \(\square\)

## 3. What \(q=1\) counting really forces

### Corollary 3.1 (global duplicate repair)

Any rethreading of this exact middle deck which ends with an injective
lower-\(q=1\) path must delete at least one old occurrence of each of

\[
 17140,\qquad12685,\qquad3868.
\tag{3.1}
\]

More generally, for two exact middle paths with the same number of edges,

\[
 e_1(T)-e_1(T')
 =
 |\operatorname{supp}(d_{T'})\setminus\operatorname{supp}(d_T)|
 -
 |\operatorname{supp}(d_T)\setminus\operatorname{supp}(d_{T'})|.
\tag{3.2}
\]

Thus a net increase of \(q=1\) support consumes repeat excess.

#### Proof

Both assertions are immediate from fixed total occurrence count. In the
H19 path the only excess occurrences are the three second copies in
(3.1), so an injective endpoint cannot retain both members of any pair.
\(\square\)

This is a theorem about improving \(q=1\) support. It says nothing about
improving the compiler matching rank.

## 4. A \(q=1\)-neutral Hall-improving counterexample

Let \(P_1\) be the frozen Hall-20 router state and \(P_2\) the authoritative
H19 state:

    P1 = scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
    P2 = scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json.

Their state hashes are respectively

    eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51
    86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b.

They are related by the legal braid

\[
 P_2=\operatorname{FR}(123,722,4710)P_1.
\tag{4.1}
\]

### Theorem 4.1 (exact shadow-neutral Hall descent)

The transition (4.1) has all of the following properties.

1. Both endpoints enumerate the exact rank-eight deck, are Johnson paths,
   are depth-three resident, and have complete upper support at every
   depth \(1\le q\le7\).
2. Their full lower and upper \(q=1\) multiplicity vectors are identical.
3. Their required lower support sets are identical at every depth
   \(1\le q\le7\).
4. All four holes (2.6), all three repeated labels (2.5), and all six
   repeated physical edges are unchanged. Their complete local
   depth-three collars are transported unchanged.
5. Nevertheless the occurrence-labelled compiler rank changes as

   \[
   16363\longrightarrow16364,
   \tag{4.2}
   \]

   so Hall deficiency drops from \(20\) to \(19\).

Consequently exact middle data, exact lower and upper \(q=1\) marginal
data, and the complete bounded \(z_{14}\) defect atlas do not force every
Hall-improving switch to repair a named sector motif. This conclusion is
about a route within the fixed noninjective \(q=1\) stratum, not about two
globally \(q=1\)-injective endpoints.

#### Proof

Every segment-interior edge survives (4.1), possibly transported. The
three deleted seams are

\[
\begin{array}{c|cc}
\text{old edge}&\lambda&\upsilon\\ \hline
18346-20266&18218&20394\\
20386-28450&20258&28578\\
26410-26530&26402&26538,
\end{array}
\tag{4.3}
\]

and the three inserted seams are

\[
\begin{array}{c|cc}
\text{new edge}&\lambda&\upsilon\\ \hline
18346-26410&18218&26538\\
20266-20386&20258&20394\\
26530-28450&26402&28578.
\end{array}
\tag{4.4}
\]

Thus both the lower multiset

\[
 \{18218,20258,26402\}
\]

and the upper multiset

\[
 \{20394,28578,26538\}
\]

are merely permuted. All six seam vertices contain \(z\), so this is an
all-\(AA\) recoupling. None of its three lower labels is one of the
repeated labels or holes in (2.5)--(2.6).

In \(P_1\), the first copies of the three repeated physical edges occur at
positions \(3181,1439,3152\); in \(P_2\) they occur at
\(2582,840,2553\). Their ordered collars are identical. The second
copies at \(5917,5046,5549\) are fixed. Hence the entire bounded atlas is
transported, not repaired.

The exact physical matching ranks (4.2), residence, and all-depth support
claims are independently established in

    THREAD_A_K15_H20_H19_PRISM_ROUTER_REMOTE_SPLITTER_20260728.md
    scratch/threadA_audit_k15_h20_h19_prism_router.py.

For completeness, the rank gain has the following explicit DM witness.
On the \(161\)-target component rooted at

\[
 v_0=24610,\quad v_1=25634,\quad
 v_2=26146,\quad v_3=26402,
\tag{4.5}
\]

cancel a common \(159\)-column bank of rank \(159\). The residual columns
change as

\[
 \{\!\{\{v_2,v_3\}\}\!\}
 \longmapsto
 \{\!\{\{v_0,v_1\},\{v_2\},\{v_3\}\}\!\}.
\tag{4.6}
\]

The old extension has rank \(160\); the two new singleton columns raise the
rank to \(161\). Physically the new columns form the consecutive
depth-\(0/1/2\) ladder at starts \(4713,4712,4711\). This proves the Hall
gain without invoking a \(q=1\) defect repair. \(\square\)

The union of the old and new seam incidences in (4.3)--(4.4) is an
alternating \(C_6\) between the three lower colours and three upper
colours. The old and new edges are two different perfect matchings:

\[
 (L_1U_1,L_2U_2,L_3U_3)
 \longmapsto
 (L_1U_3,L_2U_1,L_3U_2).
\tag{4.7}
\]

For each valid pair \(L\subset U\), \(|L|=7,|U|=9\), the two endpoints
are uniquely \(L\cup\{a\},L\cup\{b\}\), where \(U\setminus L=\{a,b\}\).
Thus (4.7) is literally a change of the paired lower/upper incidence, not
only a relabeling. Marginal lower/upper data cannot see its orientation;
the three lower and three upper labels are individually distinct inside
the packet. The paired incidence and its deeper collar can see it.

## 5. The surviving rank-seven projection theorem

The mask coincidence between \(q=1\) defects and compiler residuals has a
precise, but narrower, explanation.

### Lemma 5.1 (internal rank-seven traces project to \(q=1\))

Let \(A=(A_p)\) be any source/controller word satisfying

\[
 T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}.
\tag{5.1}
\]

For every internal carrier edge put

\[
 U_i=A_{i+1}\cup A_{i+2}\cup A_{i+3}.
\tag{5.2}
\]

Then

\[
 U_i\subseteq T_i\cap T_{i+1}=\lambda_i.
\tag{5.3}
\]

In particular,

\[
 |U_i|=7\quad\Longrightarrow\quad U_i=\lambda_i.
\tag{5.4}
\]

Therefore a rank-seven target with no \(q=1\) carrier occurrence has no
internal depth-two compiler occurrence. A first internal occurrence of a
previously internally absent rank-seven target \(Q\) must either create a
\(q=1\) edge of label \(Q\), or move from a state in which every old
\(Q\)-labelled edge collapsed to one in which some \(Q\)-labelled edge has
a rank-seven internal trace.

#### Proof

The three letters in (5.2) occur in both four-letter windows defining
\(T_i\) and \(T_{i+1}\), proving (5.3). A Johnson edge has rank-seven
intersection, so equality follows when \(|U_i|=7\). \(\square\)

The last sentence is deliberately about the **first internal occurrence**.
An additional column for an already positive target may change Hall rank
without changing \(q=1\) support or removing a collapse.

For the stored common controller

    scratch/thread_a_k15_h19_m0_a0_baseline_20260729.json,

the \(q=1\)-present labels \(4469\) and \(19098\) collapse respectively to
rank-six traces \(4213\) and \(18970\). The four \(q=1\) holes have no
internal rank-seven occurrence, while \(8877\) is rescued by the boundary
depth-one window \([0,1]\). Hence the rank-seven targets in that stored
residual are exactly

\[
 \{4469,5801,7267,13620,19098\}.
\tag{5.5}
\]

This classification is controller-specific. The carrier's middle and
\(q=1\) data do not determine which present labels collapse under a chosen
common controller.

Also, among the seven masks named in (2.5)--(2.6), the stored 21-target
compiler residual contains only

\[
 \{5801,7267,13620\}.
\tag{5.6}
\]

The duplicate labels \(17140,12685,3868\) and the boundary-rescued hole
\(8877\) are covered. Literal mask equality is therefore not a
target-cell incidence invariant.

## 6. Correct finite local replacement

For the canonical maximal-erosion/native occurrence graph at depth three,
a cell of depth \(h=0,1,2\) starting at source position \(s\) depends only
on the carrier footprint

\[
 [s-3,s+h].
\tag{6.1}
\]

If a segment rethreading transports every segment-interior profile and
changes one internal seam, at most \(h+3\) cells of depth \(h\) have
footprints crossing that seam. Hence at most

\[
 (3+4+5)=12
\tag{6.2}
\]

compiler columns per seam can change, and a three-seam braid changes at
most \(36\) old and \(36\) new columns. The transition (4.1) has \(34\)
uncancelled profiles on each side.

Indeed, the maximal erosion letter at \(p\) depends on carrier positions
\([p-3,p]\), so the union of letters \(s,\ldots,s+h\) depends on
\([s-3,s+h]\). For a seam between \(T_t,T_{t+1}\), this interval crosses
the seam exactly when

\[
 t+1-h\le s\le t+3,
\]

which gives \(h+3\) possible starts.

Thus a viable bounded local-shore theorem must classify:

1. \(q=1\) hole/repeat and controller-collapse motifs;
2. boundary rank-seven rescues;
3. shadow-neutral lower/upper matching cycles such as (4.7); and
4. the radius-five DM projections of their changed compiler columns.

The exact matching comparison is the profile-cancellation identity. If
\(\mathcal C\) is the common column multiset and
\(\mathcal E,\mathcal E'\) are the old and new exceptional multisets, then

\[
 r(\mathcal C+\mathcal E')-r(\mathcal C+\mathcal E)
 =
 \kappa_{\mathcal C}(\mathcal E')
 -
 \kappa_{\mathcal C}(\mathcal E).
\tag{6.3}
\]

This finite radius-five collar system is the correct replacement for the
false seven-mask necessity claim in the canonical occurrence graph. An
adaptively reselected common core/controller may change columns away from
the seams and is not bounded by (6.2) without an additional transport
hypothesis.

## 7. Scope

Theorem 4.1 proves that no implication based only on the exact middle deck,
the lower and upper \(q=1\) marginal data, all-depth support, and the seven
named \(z_{14}\) defects can force every Hall-improving step to repair one
of those defects.

It does **not** prove any of the following stronger statements.

1. The endpoints \(P_1,P_2\) are not globally lower-\(q=1\)-injective;
   both retain four holes and three doubles. Therefore this is not a
   counterexample to a theorem whose additional endpoint hypothesis is
   global \(q=1\) injectivity. Corollary 3.1 says that any eventual
   globally injective endpoint must repair all three doubles, but not that
   each intervening Hall gain does so.
2. The physical H20/H19 paths are not strict \(C_{15}\)-equivariant
   omission-state cycles. A theorem using essential twisted-state orbit
   closure is not refuted. Such a proof would need information absent from
   exact middle/\(q=1\) marginals.
3. The rank in (4.2) is the ordinary occurrence-labelled compiler-graph
   matching rank. The audited route simultaneously lifts the final
   positive DM shore, but it does not furnish one common source word for
   every exterior matching edge. Thus the example refutes a necessity
   claim for Hall-rank improvement; a theorem restricted to fully lifted
   common-controller improvements would need a further example or proof.

For the concrete H19 descent lane, however, the proposed stepwise motif
necessity is rigorously false. The smallest correct replacement gate is
the radius-five paired-shadow/controller-column classification in Section
6.
