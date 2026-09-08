# K17 drop-12 two-mode \(Q_{23}\) survivor cover and rank-47 replay theorem

**Date:** 2026-08-03

**Status:** exact parent-local supplier theorem, complete occurrence no-go for
all pairs containing one of the 468 rank-improving anchors, finite residual
domain decomposition, and rank-47 replay specification. The sole remaining
two-mode completeness gap is the 5,267,978-child no-\(H\), \(S\)-anchored
face. No final K17 word is claimed.

All claims are bound to the canonical compressed parent
`e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb`,
literal final
`fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c`,
and structural catalogue
`790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434`.
Phase 1 remains transported-owner evidence.

## 1. Bound finite data

The fixed semantic Hall shore \(Q\) has 23 old hard heads and two supplier
rows,

\[
N_0(Q)=\{12973,14851\}.
\tag{1.1}
\]

Their exact incidences are

\[
12973\longleftrightarrow\{12948,13148\},\qquad
14851\longleftrightarrow\{1490,15103\}.                 \tag{1.2}
\]

The head and supplier ledgers have SHA-256
`479302b36bf84710d2f5339177d28fd1db86127573646a23009c1bf6252cc5ca`
and
`5686f140d3ad542a0d5ed2df5dd832cba1427d208ec9dad21cbb6cd217be3abb`.

The fixed-bank-safe structural universe \(U\) has 112,621 modes. Its endpoint
audit has SHA-256
`1c940841e55599d81879d776705e3572d0bef6452b95f2616802eaab1123ecea`;
the compact domain audit has SHA-256
`48a2c4eef93e047c7ee43072118049ebf7adb0a1d280db7dbcb2c3427718b74b`.

The exhaustive positive-singleton score ledger has SHA-256
`84a4475d2d3d445ff8acc827cbf22ce56b539294208ab482ebe4e8e6f4308cb7`.
Its producer has SHA-256
`2882aca450fd2938648df2c3b10629b94be5f22c8e4013400d46afda2b7e3f94`.
The exact 47-row replay ledger frozen with this theorem has SHA-256
`b88010a43e2f0bba510e77c93a5cf6a6707b67f204a665bfb308d0b7ca35dc97`;
the pair-domain decomposition has SHA-256
`db6b762c8915b26eb0cf58e587019692c13c38953601ad72212398d998e93cac`.
The final host-admitting unary occurrence replay for the 468 modes in \(H\)
has source SHA-256
`92d929b0aae6a6f7e908b8ad0754e3f02871051ec78daf116094132e4ffcbf1d`,
audit SHA-256
`22947f62a855bdf32613100f294dcd541b9541ac31db06b04075e8665ba17fde`,
and manifest SHA-256
`860741486619423d87d1f685234f49692fd39a2a7025c2ead72c904cb90c4891`.

The complete directed \(H\times U\) rescue upper has request-ledger SHA-256
`3f61ed962dcdca21cb3a3412f89a9ec9de27c594e7358e7921bc7d2727ad31e5`,
audit SHA-256
`1290f68c2f39b3565643ee02174a9be6a2b1d119a9adf3dcbcf871e4bac23cff`,
and producer SHA-256
`8bc5c3448095b01a60b2296cfdc18625037c07f222a8311a0d3e67fee3e74e5d`.
The independent exact replay of its 94 survivors has audit SHA-256
`1e9a44d5336ff436e8b08c3fe8d28c2a2426430f150a5c7a335c5d69b50c92b4`,
zero-positive ledger SHA-256
`f33f6ed5a7102ee3cc63a260a0608685a6776586c8014015ad8df56c0c4421c5`,
and verifier-source SHA-256
`fee7a769f10ebc54446b9f47808e65f8f6aafd68bf093d6a1eafe1d9032b3f7c`.

## 2. Exact fixed-shore composition

For a mode \(e\), let:

- \(F_e=\{h_e,d_e\}\) be its LR-host and LMR-donor row set;
- \(D_e\subseteq Q\) be the old \(Q\)-heads retired by \(e\);
- \(B_e(u)\subseteq Q\) be the old-head incidence mask of endpoint source
  row \(u\in F_e\) after applying \(e\).

Write

\[
N_e=N_{T_e}(Q\setminus D_e),\qquad
A_e=N_e\setminus N_0(Q),\qquad
C_e=N_0(Q)\setminus N_e.                               \tag{2.1}
\]

The exact incumbent-cut credit is

\[
\gamma_e=|D_e|+|N_e|-2
        =|D_e|+|A_e|-|C_e|.                            \tag{2.2}
\]

This uses semantic completion: each retired old head in \(D_e\) receives its
own private dummy supplier. Thus the completed child neighborhood of the old
shore has size \(|D_e|+|N_e|\), and target deficiency at most 20 requires
credit at least one on this shore.

### Theorem 2.1: constant-size pair oracle

For endpoint-disjoint modes \(e,f\), put

\[
R=Q\setminus(D_e\cup D_f).
\]

Then the joint old-shore neighborhood is exactly

\[
\begin{aligned}
N_{ef}={}&
\{s\in N_0(Q)\setminus(F_e\cup F_f):B_0(s)\cap R\ne\varnothing\}\\
&{}\cup\{u\in F_e:B_e(u)\cap R\ne\varnothing\}\\
&{}\cup\{u\in F_f:B_f(u)\cap R\ne\varnothing\},
\end{aligned}                                           \tag{2.3}
\]

and

\[
\boxed{\gamma_{ef}=|D_e\cup D_f|+|N_{ef}|-2.}           \tag{2.4}
\]

Thus the fixed \(Q\) cut is composed exactly from two endpoint IDs, one
retirement mask, and two 23-bit post-incidence masks per mode. No five-cell
hypergraph or child supplier reconstruction is needed for this necessary
cut.

#### Proof

A transfer changes only its two endpoint source states. Every other source
keeps its parent incidence mask, restricted to the old heads not retired by
either mode. Endpoint disjointness makes the three source sets in (2.3)
disjoint. A hard donor in \(Q\) contributes to \(D_e\); its replacement host
head lies outside the fixed semantic shore. A hard donor outside \(Q\)
changes no surviving \(Q\)-requirement. Hence (2.3) lists every and only
joint neighbors of the active old shore, proving (2.4). \(\square\)

### Theorem 2.2: no positive pair synergy on \(Q\)

For every endpoint-disjoint pair,

\[
\boxed{\gamma_{ef}\le\gamma_e+\gamma_f.}                \tag{2.5}
\]

More exactly,

\[
\gamma_{ef}=\gamma_e+\gamma_f-|L_A(e,f)|-|L_C(e,f)|,    \tag{2.6}
\]

where \(L_A\) consists of singleton gained suppliers whose last active
\(Q\)-head is retired by the other mode, and \(L_C\) consists of old
suppliers lost only jointly.

#### Proof

Every gained supplier is a changed endpoint, so
\(A_e\cap A_f=\varnothing\). The other mode can only retire additional old
heads and therefore can only erase such a gain.

Each old supplier in (1.2) has two distinct \(Q\)-neighbors, and one transfer
retires at most one old \(Q\)-head. A singleton loss of an old supplier
therefore requires changing that supplier row. Endpoint disjointness prevents
both modes from doing so, while two separate retirements can create an
additional joint casualty. Hence singleton casualties do not cancel and
joint-only casualties are losses. Retirement sets are disjoint because the
donor endpoints are disjoint. Summing these terms gives (2.6), hence (2.5).

Concretely, row 12973 is an endpoint of no structural mode. The only modes
touching row 14851 are edges 52844 through 52850; all replace its old
\(Q\)-mask by the empty mask, their donor masks are also empty, and none
retires a \(Q\)-head. These edge cases agree with the general accounting.
\(\square\)

## 3. Exact 515-anchor cover

The exhaustive singleton screen partitions \(U\) as

\[
U=H\;\dot\cup\;S\;\dot\cup\;Z\;\dot\cup\;N,            \tag{3.1}
\]

with:

\[
\begin{array}{c|r|c|c}
\text{class}&\text{size}&\gamma&\text{unary supplier rank}\\ \hline
H&468&+1&16878\\
S&47&+1&16877\\
Z&112099&0&\text{not used for classification}\\
N&7&-1&\text{not used for classification}.
\end{array}                                             \tag{3.2}
\]

The seven negative modes are exactly canonical edges 52844 through 52850.
The 515 positive modes comprise 95 head-retirement modes and 420
third-supplier modes.

### Corollary 3.1: complete two-mode reduction

For \(e,f\in U\), every endpoint-disjoint child of supplier deficiency at
most 20 contains a mode in \(H\cup S\).

#### Proof

Target 20 requires \(\gamma_{ef}\ge1\) on the inherited semantic shore.
If neither mode is in \(H\cup S\), both singleton credits are nonpositive,
and (2.5) gives \(\gamma_{ef}\le0\), a contradiction. \(\square\)

This is a reduction to 515 anchors, not to the 468 modes in \(H\). A
rank-stagnant anchor \(s\in S\) can combine with a rank-stagnant partner.
The abstract matching

\[
G_0=\{a\!-\!x\},\qquad e:+b\!-\!x,\qquad f:+a\!-\!y
\tag{3.3}
\]

has both unary ranks equal to one and joint rank two. Therefore no
rank-additivity argument can delete the \(S\)-anchored face.

### Exact pair quantifiers

All counts below refer to **unique unordered endpoint-disjoint two-mode
children**. Directed source-by-partner incidence counts are enumeration
workloads only.

The \(H\times U\) enumeration has 52,664,349 directed incidences. Exactly
96,146 endpoint-disjoint \(H\times H\) pairs occur in both orientations, so
the \(H\)-containing face has

\[
52664349-96146=52568203                         \tag{3.4}
\]

unique children.

### Theorem 3.2: complete \(H\)-containing pair no-go

No endpoint-disjoint two-mode child in \(U\) containing a mode of \(H\) has
an exact common-phase two-ticket occurrence packing.

#### Proof

The host-admitting unary replay proves that every \(h\in H\) has an empty
common-state menu. Therefore any feasible pair \((h,p)\) must use the new LLR
host of \(p\) in one of \(h\)'s phase-specific occurrence roles. The complete
directed enumeration checks all 52,664,349 endpoint-disjoint incidences in
\(H\times U\) and leaves exactly 94 such source-rescue upper survivors.

The independent exact verifier simultaneously deletes both donors, inserts
both hosts, retains the ten incumbent LLR hosts, reserves the 20 incumbent
rows separately in each phase, admits opposite-phase-only rows at their fixed
flags, enumerates complete tuples for both new shorts, and enforces joint
phase capacity and cross-phase flag consistency. All 94 survivors have zero
partner phase-0 tuples, hence zero option-graph edges and zero exact pair
occurrence positives. This contradicts occurrence feasibility.

For an \(H\times H\) child both directed orientations occur in the complete
enumeration; directed duplication cannot hide an unordered survivor.
\(\square\)

This no-go is stronger than a supplier rejection: it closes all 52,568,203
unique \(H\)-containing children before child supplier replay, including the
3,276 pairs already excluded by the inherited \(Q\) cut.

The no-\(H\), \(S\)-containing face has:

\[
5267163\quad S\times Z,\qquad
815\quad S\times S,\qquad
329\quad S\times N.                             \tag{3.5}
\]

Hence it has 5,268,307 endpoint-anchor children, of which exactly 5,267,978
pass the fixed \(Q\) cut. The 329 \(S\times N\) pairs have joint credit zero.

Within the \(H\)-containing face, 3,276 \(H\times N\) pairs also have joint
credit zero. Therefore the exact fixed-\(Q\)-passing envelope has

\[
\boxed{52564927+5267978=57832905}                       \tag{3.6}
\]

unique children. It is a necessary-cut envelope, not a supplier or occurrence
acceptance result.

By Theorem 3.2, the 52,564,927 \(H\)-containing members of this envelope are
exact occurrence no-gos. Consequently the entire remaining two-mode
completeness gap is

\[
\boxed{5267163\ (S\times Z)+815\ (S\times S)=5267978.}  \tag{3.7}
\]

For completeness, the full endpoint-disjoint universe has 6,315,279,148
unordered pairs. The 6,257,442,638 pairs containing no positive singleton
are exact \(Q\)-cut no-gos; the remaining 3,605 anchor-negative pairs are
also exact \(Q\)-cut no-gos. These classes and counts are frozen in
`K17_DROP12_TWO_MODE_Q23_DOMAIN_DECOMPOSITION_20260803.tsv`.

## 4. The 47 rank-stagnant positive anchors

All \(s\in S\) have \(\gamma_s=1\) and full unary rank 16,877.
Twenty-five retire one old head while retaining the two old suppliers:
21 retire head 12948 and four retire head 16378. The other 22 add a third
supplier:

\[
\begin{array}{c|c|r}
\text{new supplier row}&\text{old }Q\text{-head supplied}&\text{modes}\\ \hline
6063&5831&2\\
9049&15484&1\\
12365&12310&6\\
12760&12816&2\\
12927&12948&7\\
13057&13148&1\\
18101&16378&2\\
22823&22839&1.
\end{array}                                             \tag{4.1}
\]

Their exact child signatures are:

\[
\begin{array}{c|c|c|r}
|D_s|&|N_s|&(\text{zero heads},\text{DM-shore heads/suppliers})&\text{count}\\ \hline
0&3&(18,24/3)&2\\
0&3&(19,23/2)&12\\
0&3&(20,22/1)&8\\
1&2&(19,23/2)&6\\
1&2&(19,24/3)&2\\
1&2&(19,25/4)&1\\
1&2&(19,26/5)&1\\
1&2&(20,22/1)&15.
\end{array}                                             \tag{4.2}
\]

The bounded ledger
`K17_DROP12_QPOSITIVE_RANK21_ANCHOR47_LEDGER_20260803.tsv` records every
current candidate ID, canonical edge ID, endpoints, effect, rank, zero count,
child-shore sizes, graph FNV64, and directed disjoint-partner count.

The current producer did not export the member IDs of each child DM shore.
Consequently a shore size or graph fingerprint is not a proof-safe
partner-specific cut. For each \(s\), the next generator must export the
literal child matching \(M_s\), child shore \(Q_s\), its supplier set, and DM
reachability.

As occurrence calibration only, none of these 47 lies in the old 3,483-mode
exact-common control bank. Old marginal pricing gives native-phase-0 support
only to edge 79723, transported-phase-1 support only to edge 92903, and
neither to the other 45; none is marginally positive in both. These facts do
not establish a unary or pair no-go. All 47 require the same host-admitting,
phase-specific replay used for \(H\).

### Theorem 4.1: bounded exact rank replay for an \(S\)-anchor

Fix \(s\in S\) and a maximum child matching \(M_s\) of size 16,877. After
materializing an endpoint-disjoint partner \(p\), delete from \(M_s\) every
edge invalidated by the two changed source rows and, when present, the one
replaced hard-head slot. At most three matched edges are deleted; write the
resulting matching as \(M^-\) and the deletion count as \(k\le3\).

Then the pair child has rank at least 16,878 if and only if the alternating
network of the literal pair graph relative to \(M^-\) contains at least
\(k+1\) vertex-disjoint augmenting paths.

#### Proof

\(|M^-|=16877-k\). By the matching symmetric-difference theorem, the maximum
number of vertex-disjoint \(M^-\)-augmenting paths equals
\(\nu(G_{s,p})-|M^-|\). Thus \(\nu(G_{s,p})\ge16878\) exactly when this number
is at least \(k+1\). Unit vertex capacities give an exact max-flow oracle of
demand at most four. \(\square\)

This oracle must use the literal pair graph: replacing a hard head changes an
entire column. The inherited \(Q\) test and any exported \(Q_s\) cut are
pruning only; full matching or Theorem 4.1 is acceptance.

## 5. Exact occurrence semantics

The incumbent occurrence reservations are phase-specific:

\[
|F_0|=|F_1|=20,\qquad |F_0\cap F_1|=17,\qquad
|F_0\cup F_1|=23.                                      \tag{5.1}
\]

The opposite-phase-only rows are

```text
F0 \ F1: 25:0, 3778:0, 13011:1
F1 \ F0: 37:0, 48:1, 3785:0
```

where the suffix is the incumbent flag. A row reserved only in the other
phase may be used, subject to flag-consistent cross-phase coalescing.

The two earlier negative unary screens were nonfinal:

1. the older screen excluded the 23-row union in both phases;
2. the first phase-specific screen (audit SHA
   `79a4776ab79ec8f44b45fd4374e7bd3cd0d41ddc8daa47152dfc63af88233c0a`,
   historical manifest-file SHA
   `a7eaf78bc136a6f35d0ef583fa00f2deb298bbbf1875362a638156745b445095`)
   still excluded the ten materialized incumbent LLR hosts from the witness
   bank. That historical manifest later failed two overwritten source
   entries and is cited only to identify the superseded run, not as a valid
   freeze.

The ten rows are immutable as transfer endpoints, but that does not make
their long states unavailable as occurrence witnesses. The final V2 replay
admits them, enforces (5.1), searches all exact five-cell tuples, and still
finds zero common states for every one of the 468 modes in \(H\). Thus the
unary occurrence no-go is exact for \(H\). The corresponding corrected unary
status of the 47 modes in \(S\) remains open.

### Theorem 5.1: pair-local host aperture

For legal canonical transfers \(e,f\) on this same fixed parent, with
endpoint-disjointness and the fixed unavailable-row bank unchanged, let
\(B_{e\mid f}\) be all
phase-paired same-declared-state options for \(e\) after installing \(e\) and
deleting \(f\)'s donor, but before adding \(f\)'s host. All surviving base
long rows, including admissible incumbent LLR hosts, are retained. Let
\(C_{e\leftarrow f}\) be the joint-child options for \(e\) that use the new
host of \(f\). Then

\[
\mathcal O_e^{ef}=B_{e\mid f}\;\dot\cup\;C_{e\leftarrow f}. \tag{5.2}
\]

Hence

\[
B_{e\mid f}=\varnothing
\quad\Longrightarrow\quad
\text{every feasible option for \(e\) uses \(f\)'s host}. \tag{5.3}
\]

If both directed base menus are empty, reciprocal cross-host support is
necessary.

#### Proof

Relative to the state defining \(B_{e\mid f}\), the only long state added by
the remaining operation is \(f\)'s new host. Deleting a donor has already
been accounted for. Every joint option either avoids that added row and was
already in \(B_{e\mid f}\), or uses it and lies in
\(C_{e\leftarrow f}\). \(\square\)

### Corollary 5.2: forced partner-host use for \(H\)

For every \(h\in H\) and every endpoint-disjoint partner \(p\in U\), any
feasible pair occurrence packing uses the new LLR host of \(p\) in at least
one of \(h\)'s four phase-specific predecessor/successor roles.

Indeed, the authenticated V2 unary audit makes the complete host-admitting
base menu empty. Deleting \(p\)'s donor cannot create a socket witness, so
Theorem 5.1 applies. No analogous unconditional claim is made for \(S\).
Consequently an \(H\times H\) child requires reciprocal cross-host support;
an \(H\times(S\cup Z)\) child requires at least the directed support from the
partner host into the \(H\)-anchor.

For the pair, make a bipartite graph with shores
\(\mathcal O_e^{ef}\) and \(\mathcal O_f^{ef}\). Join two options exactly
when their phase-0 footprints and phase-1 footprints are separately
capacity-compatible and every cross-phase reused row has one consistent flag.
The pair has an exact two-ticket common occurrence packing if and only if
this graph has an edge.

The old 3,483 common-mode bank remains a valid positive/control subset, but
it is not the partner universe and cannot establish completeness.

## 6. Proof-safe replay order

An exact two-mode completeness search now needs only the 5,267,978 children
in (3.7). Every child has an anchor \(s\in S\) and a partner in \(Z\cup S\);
all \(H\)-containing, negative-partner, and unanchored faces are closed. For
each residual child it must:

1. materialize both current canonical modes simultaneously from the e878
   parent and replay the ten-mode fa491 overlay;
2. preserve the 7,213 protected rows and the incumbent tickets byte-for-byte;
3. regenerate complete phase menus with (5.1), admissible incumbent LLR
   hosts, and flag-consistent coalescing; no forced-host condition may be
   imposed on \(S\) until its host-admitting unary menu is exported;
4. pass the exact two-option compatibility graph;
5. rebuild the complete supplier graph and certify rank at least
   \(16878/16898\), using Theorem 4.1 for \(S\)-anchors when its matching
   ledger is available.

A replay-ready per-mode ledger needs

```text
edge_id, lr_row, lmr_row, H/S/Z/N class,
D_Q, post_Q_mask(lr), post_Q_mask(lmr), gamma_Q,
corrected unary phase/state option digest,
and, for S, matching plus DM head/supplier identities.
```

A pair ledger needs

```text
two edge IDs, endpoint-disjointness,
joint D_Q/N_Q and gamma_Q,
k invalidated anchor-matching edges, augmenting-flow value,
B_e|f and B_f|e digests, cross-host option counts,
option-graph edge or chosen four witnesses,
protected/incumbent replay hashes,
full child rank and matching hash.
```

The theorem closes the entire two-mode face with no positive-\(Q\) singleton,
all 3,605 anchor-negative pairs, and every one of the 52,568,203 unique
\(H\)-containing pairs. It leaves exactly the 5,267,978-child \(S\)-anchor
face: the corrected unary menus for \(S\), joint occurrence packing, and
complete supplier replay remain open. It makes no additive action-credit,
matroid, chronology, residence, compiler, or K17 optimality claim.
