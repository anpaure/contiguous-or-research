# High-congestion clean-\(C_8\) atlases: the full-overlay dichotomy

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Put

\[
 B=C_s,\qquad A=C_{s-3},\qquad n_s\le 2s+O(\sqrt s).
\tag{0.1}
\]

The canonical suffix catalogue consists of \(A\) pairwise
vertex-disjoint clean \(C_8\) cores \(R_a\), each with four root rows.
Suppose two anchored exact factors \(F^0,F^1\) are proposed as the two
shores of one bounded-span physical completion of this catalogue. Let
\({\cal K}\) be their full state-and-colour ownership components, and put

\[
 b_K=|K|,\qquad
 D_K=\sum_{P\in K}d(P),\qquad
 \Xi(F^0,F^1)={1\over B}\sum_K b_KD_K,
\tag{0.2}
\]

where \(d(P)\) is rooted adjacent-transposition distance between the two
final **full ambient** cyclic words at root \(P\).

After all crossing collars, mixed windows, and equal-target cancellations
have been combined, let \(T_{\rm cpl}\) be the number of surviving
carrier units which are **shore-coupled** to their claimed clean router.
The precise definition is in Section 2. Then

\[
 \boxed{T_{\rm cpl}\le n_s B\,\Xi(F^0,F^1).}
\tag{0.3}
\]

This inequality permits arbitrary overlap of payload strands, arbitrary
reuse of one changed occurrence by several routers, arbitrary component
mergers, and arbitrary target cancellations. Reuse by several routers
does not evade the bound: their pairwise disjoint core roots all enter the
same full component and increase \(D_K\).

Let \(\Gamma\) be the one joint retention coefficient **after** this
endpoint aggregation and de-duplication, and let \(\kappa\) be the
physical serial packing coefficient. The hard growing-packet ledger asks
for total clean-bank mass

\[
 T_{\rm req}
 =A\left({14\sqrt\pi\over\Gamma\kappa}+o(1)\right)s^{3/2}.
\tag{0.4}
\]

Carrier units which are not shore-coupled are independent background
units. After removing free multiple attribution of the same physical
occurrence, their total is at most \(n_sB\). Consequently every genuine
joint atlas meeting (0.4) satisfies

\[
 \boxed{
 \Xi(F^0,F^1)
 \ge {T_{\rm req}-n_sB\over n_sB}
 =\left({7\sqrt\pi\over64\Gamma\kappa}+o(1)\right)\sqrt s.}
\tag{0.5}
\]

In particular it cannot satisfy the terminal sparse-edit requirement
\(\Xi=o(\sqrt s)\). If every surviving clean router retains all four
changed core rows in its carrier component, the constant in (0.5) is four
times larger:

\[
 \Xi\ge
 \left({7\sqrt\pi\over16\Gamma\kappa}+o(1)\right)\sqrt s.
\tag{0.6}
\]

Thus the \(\Delta_s=\Omega(\sqrt s)\) escape left by the row-incidence
count is closed for a genuine joint clean-\(C_8\) atlas.

There is a real but nonproductive exception to the bare implication
“high congestion implies large \(\Xi\)”. A high-multiplicity payload may
remain in full-overlay components disjoint from the router cores, or
successive router edits may cancel to the identity in the final pair.
Then \(\Delta_s\) can be arbitrarily large while \(\Xi=0\) or \(O(1)\).
The exact overlap pattern is block diagonal in the final ownership
overlay: apart from a collection carrying only
\(o(Bs^{3/2})\) coupled credit, every high-multiplicity payload column is
disconnected from the router cores which claim it, and the remaining
router histories are final ownership coboundaries. Such a payload is
present only once in the physical histogram and cannot be multiplied by
the number of router labels. It therefore supplies only \(O(n_sB)\), a
factor \(\Theta(\sqrt s)\) below (0.4).

This is an endpoint theorem. It does not assume that unsigned
stage-by-stage carriers add, and it does not infer a final component from
a transient switch.

## 1. Final occurrences and target cancellation

Fix a protected depth. A pointed occurrence is a pair

\[
                         \omega=(P,h),
\tag{1.1}
\]

where \(P\) is a root row and \(h\) is an ambient cyclic start. In the
bounded-span normalization there are at most \(n_s\) relevant starts on
one row. Let \(T^e(\omega)\) be the complete ambient target of this
occurrence on shore \(e\), including every moving exterior and crossing
collar.

Call \(\omega\) changed when

\[
                         T^0(\omega)\ne T^1(\omega).
\tag{1.2}
\]

For a proposed router carrier, first sum all signed target vectors and
then cancel equal targets with opposite signs. Since the histograms are
integral, every surviving positive unit can be assigned to one changed
pointed occurrence. Therefore a carrier supported on a set \(S\) of root
rows has mass at most

\[
                         n_s|S|.
\tag{1.3}
\]

This is the final-minus-initial occurrence count. An intermediate target
which is changed at several stages but restored at the endpoint contributes
nothing. Two changed occurrences which give opposite contributions to the
same target also contribute nothing after cancellation. Thus (1.3)
already contains both stage cancellation and target cancellation.

The same physical occurrence may appear in the bookkeeping lists of
several routers. There are only two legitimate interpretations.

1. It is one background occurrence, independent of those router shore
   choices. It is then counted once in the physical carrier.
2. Its shore is locked to each router which claims it. The full ownership
   overlay must then record those dependencies, and the relevant router
   cores and the occurrence row lie in one component.

Counting it once for every router while imposing neither alternative is
free word assignment, not a physical carrier ledger.

More formally, write the actual endpoint carrier as

\[
                         \Delta=\sum_{\omega}\delta_\omega,
\tag{1.4}
\]

where every physical pointed occurrence has coefficient one. A
router-labelled extraction from this histogram is a family of weights
\(x_{a,\omega}\in[0,1]\) satisfying

\[
                         \sum_a x_{a,\omega}\le1
\tag{1.5}
\]

whenever \(\omega\) is not shore-coupled to those routers. Integral
extraction has \(x_{a,\omega}\in\{0,1\}\). Equation (1.5) merely says that
the labelled extraction is a submeasure of the physical histogram. If
one instead assigns coefficient one to the same decoupled occurrence for
\(t\) routers, the labelled sum contains \(t\delta_\omega\), not the
physical term \(\delta_\omega\) in (1.4). Such a multiplicity must either
be divided out by the joint retention coefficient or justified by
persistent shore coupling, in which case Section 3 charges it to
\(\Xi\).

## 2. Shore coupling is exactly a full-component condition

The four-root core of router \(a\) is denoted by \(R_a\). The suffix-bank
theorem gives

\[
                         R_a\cap R_{a'}=\varnothing
                         \quad(a\ne a').
\tag{2.1}
\]

For a full ownership component \(K\), say that router \(a\) is active in
\(K\) when

\[
                         K\cap R_a
\quad\hbox{contains a root }P\hbox{ with }d(P)>0.
\tag{2.2}
\]

A surviving carrier unit claimed by \(a\), represented by an occurrence
on row \(P\), is **shore-coupled** when the component \(K(P)\) containing
\(P\) makes \(a\) active in the sense of (2.2).

This is the exact independence test supplied by the full overlay. Indeed,
every component shore can be selected independently while retaining an
exact anchored factor. If \(K(P)\) contains no changed root from \(R_a\),
switch the shore of \(K(P)\) and keep every other component fixed. Any
core rows of \(R_a\) which happen to lie in \(K(P)\) have \(d=0\), so the
router core remains unchanged while the payload occurrence changes.
Hence the payload sign is not forced by router \(a\); it is an independent
background edit. Conversely, any persistent owner path tying the payload
to a changed core root lies in one full component and satisfies (2.2).

Transient owner paths do not qualify. If later stages cancel every
cross-owned state and colour, the final overlay splits and its shore
choices become independent. This is why the full final overlay, rather
than the union of historical stage graphs, is mandatory.

## 3. The component charge

For \(a\) active in \(K\), let \(c_{a,K}\) be the number of surviving
carrier units of router \(a\) represented by changed occurrences on rows
of \(K\). A unit is counted at most once for a fixed router. It may be
counted for several routers; this is the overlapping-strand case.

Let

\[
                         t_K=\#\{a:a\hbox{ is active in }K\}.
\tag{3.1}
\]

There are \(b_K\) rows in \(K\), each with at most \(n_s\) relevant
pointed starts. Hence, for every active router,

\[
                         c_{a,K}\le n_sb_K,
\tag{3.2}
\]

and therefore

\[
                         \sum_a c_{a,K}\le n_sb_Kt_K.
\tag{3.3}
\]

By (2.1), the active routers counted by \(t_K\) supply distinct changed
core roots in \(K\). Each such root has adjacent-edit distance at least
one. Consequently

\[
                         D_K\ge t_K.
\tag{3.4}
\]

Combining (3.3)--(3.4) gives the componentwise estimate

\[
                         \sum_a c_{a,K}
                         \le n_sb_KD_K.
\tag{3.5}
\]

Summation over \(K\) proves

\[
 T_{\rm cpl}=\sum_{K,a}c_{a,K}
 \le n_s\sum_Kb_KD_K
 =n_sB\Xi,
\tag{3.6}
\]

which is (0.3).

The same variables give an explicit merger penalty. Component \(K\)
contains at least one distinct core root for each of its \(t_K\) active
routers, so \(b_K\ge t_K\). Together with (3.4),

\[
 \boxed{B\Xi=\sum_Kb_KD_K\ge\sum_Kt_K^2.}
\tag{3.6a}
\]

Thus a component joining \(t\) clean cores alone costs at least \(t^2/B\)
in \(\Xi\), before any payload edit distance is charged. If all four core
rows persist in the component, the corresponding bound is
\(B\Xi\ge16\sum_Kt_K^2\).

This proof is insensitive to all overlap patterns. If one payload row is
coupled to \(t\) router cores, those cores lie in its component and
\(D_K\ge t\). If different payload blocks bridge two previously separate
router groups, their full components merge and \(b_K\) increases. Either
event raises, rather than lowers, the right side of the exact moment.

There is a useful stronger form. If every router active in \(K\) retains
all four of its core rows as changed roots in that same component, then

\[
                         D_K\ge4t_K
\tag{3.7}
\]

and (3.5) improves by a factor four:

\[
                         T_{\rm cpl}
                         \le {n_sB\over4}\Xi.
\tag{3.8}
\]

No assumption about distinct payload rows is used in either estimate.

## 4. Supply/demand substitution

The exact dense-bank carrier requirement is

\[
 M_*=\left({14\sqrt\pi\over\Gamma\kappa}+o(1)\right)s^{3/2}
\tag{4.1}
\]

per router on average. Thus (0.4) holds. On the other hand,

\[
 {A\over B}={C_{s-3}\over C_s}
 ={1\over64}(1+O(s^{-1})),
 \qquad
 n_s=(2+o(1))s.
\tag{4.2}
\]

A decoupled physical occurrence has total router-allocation weight at
most one by (1.5). There are at most \(n_sB\) such occurrences over the
whole root fibre. Therefore

\[
                         T_{\rm cpl}
                         \ge T_{\rm req}-n_sB.
\tag{4.3}
\]

Equations (3.6), (4.1)--(4.3) yield

\[
\begin{aligned}
 \Xi
 &\ge {A M_*-n_sB\over n_sB}\\
 &= {C_{s-3}\over C_s}
    {\left({14\sqrt\pi\over\Gamma\kappa}+o(1)\right)s^{3/2}
      \over(2+o(1))s}-1\\
 &=\left({7\sqrt\pi\over64\Gamma\kappa}+o(1)\right)\sqrt s,
\end{aligned}
\tag{4.4}
\]

because the subtractive \(1\) is \(o(\sqrt s)\). This proves (0.5).
Using (3.8) instead proves (0.6).

If the carrier is summed over a hereditary set \(I\) of protected depths,
both \(T_{\rm req}\) and the occurrence bound acquire the same factor
\(|I|\); (4.4) is unchanged. Separately cancelling targets at different
depths cannot improve the estimate because the allocation is performed
after cancellation at each depth.

The comparison also recovers the earlier congestion theorem. A router
needs at least

\[
 {M_*\over n_s}
 =\left({7\sqrt\pi\over\Gamma\kappa}+o(1)\right)\sqrt s
\tag{4.5}
\]

distinct support rows if its carrier is considered separately. Since
there are only \(B\) rows for \(A=(1/64+o(1))B\) routers, row congestion
is at least

\[
 \left({7\sqrt\pi\over64\Gamma\kappa}+o(1)\right)\sqrt s.
\tag{4.6}
\]

The new point is that the only possible use of this forced overlap is now
charged. Persistent overlap merges full components and gives (4.4);
nonpersistent overlap is decoupled and is counted only once in (4.3).

## 5. The exact structured exception

The statistic \(\Delta_s\) records how many proposed router supports
contain a row. It is not an endpoint invariant. Therefore no theorem of
the form

\[
                         \Delta_s\ge c\sqrt s
                         \Longrightarrow
                         \Xi\ge c'\sqrt s
\tag{5.1}
\]

is true without a coupling or noncancellation hypothesis.

For example, take any exact bounded-root packet \(Q\) and follow it by its
inverse, repeating this pair \(k\) times on the same rows. The historical
row congestion is \(2k\), while the final pair is identical and

\[
                         \Xi=0.
\tag{5.2}
\]

Leaving one final bounded-root packet uncancelled gives
\(\Delta_s=2k+1\) and \(\Xi=O(1/B)\) for one block, or \(O(1)\) for a
positive-density bounded-block bank. The same phenomenon occurs when a
fixed payload component is merely listed under many router names: its
physical endpoint histogram contains the payload once.

In the final full-overlay incidence matrix, every small-\(\Xi\),
high-congestion exception must have the following form, up to deleting an
\(o(1)\) fraction of the demanded mass.

Indeed, \(\Xi=o(\sqrt s)\), \(n_s=O(s)\), (3.6), and (3.6a) imply the two
exact necessary estimates

\[
 \sum_{K,a}c_{a,K}=o(Bs^{3/2}),
 \qquad
 \sum_Kt_K^2=o(B\sqrt s).
\tag{5.3}
\]

* The nontrivial final ownership components are bounded or have small
  edit-weighted component moment.
* The total credit in payload components which also contain changed
  claimed core roots is \(o(Bs^{3/2})\). This is the exact consequence
  \(T_{\rm cpl}\le n_sB\Xi\) when \(\Xi=o(\sqrt s)\).
* Any historical owner edge which did connect it to the other router
  cores is canceled by a later inverse edge, so it is absent from the
  final overlay.
* The carrier multiplicity is therefore located in repeated columns of a
  router--payload incidence table, not in distinct endpoint occurrences.

Equivalently, after contracting the final full components, the incidence
table is block diagonal on its genuinely coupled entries; every remaining
high-multiplicity column is a decoupled background column. This is the
precise exception pattern. It is compatible with small \(\Xi\), but its
total physical carrier is at most \(n_sB=O(sB)\), whereas (0.4) is
\(\Theta(Bs^{3/2})\).

## 6. Decision for the clean-\(C_8\) amplifier lane

The bounded-span clean-\(C_8\) amplifier now has a complete dichotomy.

1. If the \(\Theta(\sqrt s)\) carrier amplification is physically tied to
   the clean router shores, (0.5) gives
   \(\Xi=\Omega(\sqrt s)\), contradicting the required
   \(o(\sqrt s)\) sparse-edit moment.
2. If the shared carrier is not so tied, independent full-component shore
   choices separate it from the routers. Its occurrences are common
   background and can be counted only once; their total is
   \(O(sB)=o(Bs^{3/2})\).
3. If the apparent gain is stagewise and disappears after endpoint or
   target cancellation, it is not carrier mass in the first place.

Overlapping strands and target cancellations therefore do not create a
third case. They respectively produce component merger, decoupled reuse,
or loss of final carrier. Hence the clean bounded-span \(C_8\) amplifier
family cannot simultaneously meet the hard carrier ledger and the
terminal sparse-edit condition.

This does not address a macroscopic-span packet, whose number of starts
and parent-context density must both be recomputed, nor a different dense
router catalogue. It closes precisely the high-congestion escape left by
the bounded-span clean suffix-\(C_8\) construction.
