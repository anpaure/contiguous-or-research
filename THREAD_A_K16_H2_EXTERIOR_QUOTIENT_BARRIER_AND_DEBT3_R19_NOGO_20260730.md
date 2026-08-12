# K16 H2 strict exterior-return quotient barrier and collateral-three R19 theorem

Date: 2026-07-30  
Lane: A  
Status: exact exterior state-space lower bound; exact collateral-three retained-donor no-go

## 1. Frozen source and strict exterior shell

All positions are zero-based.  The source is the authenticated
length-$12873$ word

~~~text
scratch/k16_ejection_lns_h2_p110_20260730.word
SHA-256 5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7
~~~

with holes $0x4879,0x6879$.  Let $R19$ be the nineteen return cells

\[
[576,578]\cup[3329,3331]\cup[3494,3496]\cup
[3838,3840]\cup[5463,5466]\cup[5971,5973].                 \tag{1.1}
\]

For strict physical-support separation from the delete-$p1$ collar lane,
put

\[
C=[0,5)\cup[6435,6444)\cup[12869,12873),\qquad |C|=18.    \tag{1.2}
\]

In particular $6440\in C$.  Of the twenty collateral-exactly-two donor
rows, exactly one has its donor cell in $C$:

\[
12872:082a,\qquad D=\{ce61,ce63\}.                         \tag{1.3}
\]

That row is excluded.  The strict shell retains seventeen ordinary donors
outside $R19$ and two internal donors at $3496,5971$.

For each retained donor, keep the donor at its atlas value, choose one of
the eight fixed services at $5462$, make exactly one changed return in
$R19$ (not the donor when it is internal), and exactly one changed exterior
return.  The exterior cell lies outside $R19$, $C$, the service cell, and
the donor cell.  Both return values are arbitrary nonzero masks different
from their incumbents.

Thus all final words have four distinct edited sites.  This excludes the
support-at-most-three/radius-three lane, Lane D's $p6440$ strata, every
collar-594 site, and all larger rethreads.

For an ordinary donor there are $19$ inner and $12834$ exterior choices.
For an internal donor there are $18$ inner and $12835$ exterior choices.
Therefore the strict raw position state space is

\[
17\cdot8\cdot19\cdot12834+
2\cdot8\cdot18\cdot12835
=36859536.                                                   \tag{1.4}
\]

This stricter interpretation is used throughout.  Source-family separation
alone would already separate the H2 and collar-594 candidate families, but
would permit support positions in $C$: the two frozen sources differ at
exactly $2544$ coordinates, whereas the union of their allowed edit supports
has size at most $4+18=22$, so their output families cannot intersect.  That
weaker source-separated face is not claimed here.

## 2. Exact literal-transfer quotient

Fix a base $V$ and an ordered pair $p<q$.  Let

\[
K(V;p,q)=\{T\ne0:\text{ no }T\text{-witness avoids both }p,q\}. \tag{2.1}
\]

Partition the affected intervals into $p$-only, $q$-only and both-cell
classes.  Their exact Boolean profiles are

\[
X_T(a),\qquad Y_T(b),\qquad Z_T(a\lor b).                  \tag{2.2}
\]

The $Z$ family is retained exactly when a literal both-cell context can be
active for some allowed changed pair.  Include also the two incumbents
$u=V_p,v=V_q$.  Write

\[
\Sigma(V;p,q)=(K,X,Y,Z_{\rm active},u,v).                  \tag{2.3}
\]

**Theorem 2.1 (literal-transfer quotient).**  If two pair instances have
identical signatures (2.3), then they have identical sets of completing
literal value pairs $(a,b)$.  Hence one maximum-envelope/coatom solve per
signature is exact, and any positive values transfer verbatim to every
instance in the class.

*Proof.*  For every $T\in K$, the edited word covers $T$ exactly when

\[
X_T(a)\lor Y_T(b)\lor Z_T(a\lor b)=1.                      \tag{2.4}
\]

Targets outside $K$ retain an avoiding witness.  The incumbents specify the
two forbidden values.  Every datum in (2.4) and both domain deletions is
therefore identical under equality of (2.3).  \(\square\)

For fixed $a$, let $D_a$ be the targets not supplied by $X(a)$ and put

\[
M_a=\bigcap_{T\in D_a}T.                                   \tag{2.5}
\]

Every completing $b$ lies below $M_a$, and coverage by $Y(b)$ or
$Z(a\lor b)$ is upward-monotone there.  Thus it is exhaustive to test
$M_a$, or its nonzero coatoms when $M_a$ is the forbidden incumbent.  If
$M_a=0$, no nonzero completion exists.  Joint-inactive kernels may group
identical $X$ profiles; joint-active kernels retain each literal first value
because $Z$ also depends on $a\lor b$.

## 3. Hole recovery and the exact projected lower bound

The signature itself recovers the base-hole ledger.  Evaluate (2.4) at the
two incumbents.  For a critical target, this reconstructs all original
witnesses meeting the pair.  The only possible concern is omission of an
inactive $Z$ family.  In the H2 word every $R19$ incumbent has Hamming weight
between three and five.  Hence a both-cell incumbent witness has a target of
weight at least three, and the exact joint-activity condition retains $Z$.
Consequently

\[
H(V)=\{T\in K:X_T(u)=Y_T(v)=Z_T(u\lor v)=0\}.              \tag{3.1}
\]

Thus the hole ledger and ordered incumbents are invariants of the exact
literal-transfer quotient.

Now restrict only for a lower bound to the common exterior tail

\[
Q=[5974,12868]\setminus C.                                 \tag{3.2}
\]

It has $6886$ positions and $5760$ distinct source incumbents.  Removing a
uniquely valued donor position leaves $5759$; otherwise all $5760$ remain.
Every $q\in Q$ follows every $R19$ cell, and the allowed $R19$ incumbents are
pairwise distinct.  Hence distinct pairs of an $R19$ incumbent and a tail
incumbent give distinct signatures.

The nineteen retained donor rows have eighteen distinct post-service hole
ledgers.  Their exact contribution is

\[
11(19)(5760)+5(19)(5759)+2(18)(5760)=1958305.              \tag{3.3}
\]

**Theorem 3.1 (projection barrier).**  The strict exterior shell contains at
least $1958305$ distinct signatures of the literal-transfer
maximum-envelope quotient (2.3).

*Proof.*  Choose one donor representative for each of the eighteen hole
ledgers and one fixed service.  Equation (3.1) separates different ledger
classes.  Within a class, the ordered incumbent coordinates separate every
combination counted in (3.3).  All selected combinations are legal members
of the strict shell, so their signatures are distinct.  \(\square\)

The value $1958305$ is the exact number of distinct displayed
hole/incumbent projection tuples on the deliberately selected subfamily in
the proof: one donor representative and one service for each of the eighteen
hole ledgers, every legal $R19$ return, and the common tail $Q$.  Different
positions with the same incumbent may create further signatures, so no
sharpness is claimed for the subfamily's full signature count, the full
strict-shell projection, or the full-shell signature count.  The theorem
does not rule out a future symbolic solver which abandons literal witness
transfer, but it proves that the current exact kernel cache cannot compress
the exterior face to a sub-million auditable state space.  Accordingly the
exterior solve was not launched.

The solver-free arithmetic/provenance audit is

~~~text
scratch/audit_threadA_k16_h2_strict_exterior_kernel_projection_20260730.py
SHA-256 1241be3b3456dc37f29b50647d7c75d8a8639c52d9248436113277d57492d10f
scratch/threadA_k16_h2_strict_exterior_kernel_projection_20260730/projection.audit.json
SHA-256 0ba2f67ae901f503b39949456fd813aff3ed67325acf9ff9788f0a9ad9de3c73
~~~

It independently verifies (1.4), all eighteen projection rows, (3.3), the
$R19$ weight range, and every parent hash.

## 4. Collateral-three pivot: exact catalogue and scope

The authenticated reserve atlas has exactly twenty-nine rows with collateral
exactly three, all on distinct positions and all assigning $0x082a$.  Their
positions and debt triples are listed below; all masks are hexadecimal.

\[
\begin{array}{r|l@{\qquad}r|l}
58&186b,386b,387b&1659&682a,68aa,68ae\\
2130&0f2a,0f32,4f32&2131&0da9,0dad,4dbd\\
2294&0c2a,1c6a,3c6a&2692&494a,594a,5d4a\\
3495&506e,507e,547e&3547&2b2a,2baa,2bab\\
3985&20ae,20af,30af&4198&29ca,2bca,2bce\\
5649&0408,4caa,5caa&5650&4d2a,6d2a,6d3a\\
5935&1c2c,1c6c,3c6c&6496&986b,b86b,b87b\\
6854&993c,997c,b97c&7003&aca9,aea9,aead\\
7496&9839,9c39,9e39&7752&e85a,ec5a,ecda\\
8568&8f2a,8f32,cf32&9123&8ca8,8ce9,8ced\\
9130&c94a,d94a,dd4a&10423&a0ae,a0af,b0af\\
10636&a9ca,abca,abce&10944&c872,c972,cb72\\
10965&a43b,b43b,b63b&11217&a820,ba62,ba72\\
11823&91ab,d1ab,d1eb&12087&8408,ccaa,dcaa\\
12373&9c2c,9c6c,bc6c&&
\end{array}                                                   \tag{4.1}
\]

Only donor $3495$ lies in $R19$.  No donor lies at $5462$, $6440$, or in
$C$.  Fix one donor at $0x082a$, choose one of the eight services, and make
exactly two distinct arbitrary nonzero changed returns in $R19$, deleting
$3495$ from the return set for that donor.  The donor is retained.

This again has four distinct edited sites and is disjoint from the
support-at-most-three/radius-three, Lane-D, collar-594, exterior-return and
larger-rethread lanes.

## 5. Exact base ledger and two-return criterion

**Lemma 5.1 (debt-three base replay).**  Every one of the
$29\cdot8=232$ donor/service bases has exactly six holes:

\[
\{486b,686b,6c6b\}\cup D,                                  \tag{5.1}
\]

where $D$ is its atlas debt triple.  The twenty-nine resulting ledgers are
distinct and service-independent.  Every inter-$R19$ gap retains OR
$0x7fff$, with fixed avoiding witnesses for $0x7fff$ and $0xffff$.

*Proof.*  The engine first verifies each donor-only ledger against the full
source multiplicities, then freshly replays each donor/service base.  It
records rather than assumes the base holes.  Independent aggregation of all
232 output rows gives (5.1).  \(\square\)

For each return pair, the critical set $K$, all three context families, and
semantic $Z$ activity are recomputed from the literal base.  Criterion (2.4)
and the envelope/coatom theorem therefore apply without a marginal or
hard-coded-hole assumption.

## 6. Exact collateral-three exhaustion

**Theorem 6.1 (collateral-three retained-donor no-go).**  No word in the
scope of Section 4 is universal.

*Proof.*  The twenty-eight ordinary donors contribute

\[
28\cdot8\binom{19}{2}
\]

kernels.  Internal donor $3495$ contributes

\[
8\binom{18}{2}.
\]

Thus the exact totals are

\[
39528=34672\text{ cross-block}+4856\text{ same-block},      \tag{6.1}
\]

representing

\[
39528\cdot65534=2590427952                                \tag{6.2}
\]

raw first values.  All cross-block kernels are joint-inactive; all 4856
same-block kernels retain $Z(a\lor b)$.

The exact cache has $8588$ kernel keys and $30940$ identity hits.  It
evaluates $319658042$ retained first rows and $311199402$ second
envelopes/coatoms.  There are $8477864$ compressed first-profile
representatives with zero target intersection, no empty-deficit shortcut,
and maximum critical-set size $39$.

All 232 cases and all 39528 kernels are visited.  The witness is null, so
(2.4) fails for every permitted assignment.  \(\square\)

## 7. Authentication and independent audit

The final engine is

~~~text
scratch/search_threadA_k16_h2_debt3_r19_tworeturn_mitm_20260730.cpp
SHA-256 e843f055669c85064c2910b0862527be5d6000824cb1f4b90066478dda1d0e24
~~~

and includes the audited R19 kernel source with SHA-256

~~~text
644ff89cba87372db01420ba8c61c1794065e6c1a37c4677bf348d5db3f80fd3.
~~~

An independent pre-run audit matched all twenty-nine hard-coded rows against
the frozen atlas and checked the scope, dynamic ledgers, cache identity,
joint activity, fail-closed target cap, counters, and candidate-replay branch.

Two fresh H100 `/home` runs used one CPU, a $4$ GiB address-space cap, a
$1$ GiB output cap and an $1800$-second timeout.  They exited zero in $11.41$
and $11.30$ seconds, used $10404$ and $10400$ KiB maximum RSS, incurred no
swap, emitted no candidate, and produced byte-identical audits:

~~~text
scratch/threadA_k16_h2_debt3_r19_tworeturn_mitm_20260730/run1.audit.json
scratch/threadA_k16_h2_debt3_r19_tworeturn_mitm_20260730/run2.audit.json
SHA-256 d23c86f8ca6217ae551892d73981981bc8f8c1b4b67fd64739d3637a6f082339
~~~

The compiled binary has SHA-256

~~~text
760ba1c12a1409b017bafdab6a757a8dedd9cba7ea0aee57950d0ac8e8f1b698.
~~~

A separate copied-artifact audit checked every case row, all aggregate
counts, resources, hashes, and the absence of a candidate.

## 8. Exact boundary

The exterior result is a lower bound for the current literal-transfer
maximum-envelope quotient, not an unrestricted exterior-return no-go.  A
different symbolic quotient or the full strict exterior face remains open.

The collateral-three theorem closes all twenty-nine exact-three donors only
for a retained donor, eight fixed services, and exactly two $R19$ returns.
It does not decide support at most three, collateral at least four, exterior
returns, three or more returns, or global rethreads.

No global bound changes.  The bracket remains

\[
12873\le\nu(16)\le12874.
\]
