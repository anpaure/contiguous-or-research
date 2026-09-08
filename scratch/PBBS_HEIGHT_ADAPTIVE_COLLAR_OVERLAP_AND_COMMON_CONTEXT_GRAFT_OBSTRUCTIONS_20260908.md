# Literal overlap and common-context grafts for height-adaptive PBBS words

2026-09-08. Pure constructive-interface analysis by `exact_b_induction`.
No mathematical program was run. This note identifies exact obstructions
to two specified gluing families, not to arbitrary changes of the letters
or to the all-k equality conjecture.

The input is the proved construction in
`HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md`: canonical upper owners
`X_i=A_i^c`, with `A_(i+1)=gA_i`, and literal letters
`D_i=intersection_(j=0)^H X_(i+j)` on a cycle of height `h>=H>=1`.
The original height-adaptive word uses `H=h`. The local lemmas below
also apply to a common smaller aperture `H` on several cycles.

## 1. Exact short ranks and the two globally unique windows

Every positive coordinate run of X has length at least `h+1`.
During any `q<=H` successive Johnson transitions, the removed coordinates
are distinct members of the initial owner. Indeed, removing a coordinate
inserted during these transitions, or removing the same coordinate twice,
would exhibit a positive run of length at most `q-1<h+1`. Consequently

    |intersection_(j=0)^q X_(i+j)|=r+1-q.

The exact erosion identity therefore gives, for `1<=ell<=H+1`,

    |D_i union ... union D_(i+ell-1)|=r-H+ell.

In particular every letter has rank `r+1-H`. A backward H-letter window
ending at i is `X_i intersection X_(i+1)=fA_i`, of rank r; the analogous
H+1-letter window is `X_i`, of rank r+1. As i ranges over all canonical
cycles, each of these two layer labels appears exactly once: both A and
fA are permutations of the complete middle layer.

An H+2-letter window is the union of two distinct adjacent owners and
has rank r+2. Thus in the unmodified bank the rank-(r+1) targets have
exactly the H+1 window length.

## 2. A sharp restriction on literal overlaps of fully opened blocks

The operation under consideration emits each full block consisting of
one D period and its first `2h-1` letters, and glues these linear blocks
by identifying equal suffix/prefix strings. Every original block remains
a contiguous literal substring. Such identification really preserves
every old interval witness, so it is a legitimate all-rank construction.
Arbitrary cycle cuts, reversals, ordering, and overlap lengths are allowed.

For the original aperture H=h, blocks of different heights have letters
of different ranks, hence have no nonempty literal overlap. Two distinct
cycles at the same height H cannot share an H-letter string: its OR would
be the same globally unique rank-r facet. Thus their overlap is at most
`H-1` letters. This remains true on reversing either word.

Let c_H count cycles at height H. There are at most `c_H-1` same-height
joins for each occupied height. Hence every word obtained by this
overlap-only method has length at least

    W_r + sum_H c_H(2H-1) - sum_(c_H>0) (H-1)(c_H-1)
      = W_r + sum_H H c_H + sum_(c_H>0)(H-1).

The verified k17 histogram in
`K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md`
has all heights 1 through 8 present and `sum H c_H=519`. Therefore this
entire family has

    N >= 24310+519+28 = 24857 > B(17)=24313.

This is a restriction on identifying identical literal substrings of
the fully opened blocks. Trimming witnesses and repairing them elsewhere,
changing letters, or introducing new seams with different contexts is
outside its scope.

## 3. The shorter common-context zero-extra graft also fails

Fix `H>=2`. Take one cut `i -> i+1` in each of several distinct canonical
cycles with the same aperture H. Suppose the last H-1 literal letters
before every cut form the same string C. Write U for its OR; Section 1
gives `|U|=r-1`.

At port i, its rank-r source facet and destination facet have the forms

    F_i=U+{x_i},       G_i=U+{z_i},

and the old middle owner at the destination is

    T_i=U+{x_i,z_i}.

All source and destination positions are distinct (one cut per distinct
cycle), and the global rank-r palette is injective. Consequently the
`x_i` are distinct, the `z_i` are distinct, and the two label banks are
disjoint. In particular `x_i!=z_j` for every i,j.

Now permute the outgoing destinations without adding or changing letters.
The shared H-1 context makes every H-letter suffix vector at each entered
destination exactly its old one, and all subsequent unchanged letters
transport it. Thus all rank-r windows remain unchanged. The only altered
H+1 windows are the immediate seam owners, which become

    T_i'=U+{x_i,z_(pi(i))}.

Because the two arm banks are disjoint, equality with an old owner T_j
forces `x_i=x_j` and `z_(pi(i))=z_j`, hence `j=i` and `pi(i)=i`.
Therefore preserving the old middle-owner set forces the identity
permutation. No nontrivial cycle fusion is possible in this family.

This is a literal middle-coverage obstruction, not just loss of a selected
witness. Every interval of length at most H has rank at most r because
the H-windows are retained. Any rank-(r+1) interval of greater length
contains an H+1 subwindow and must equal its OR. All H+1 subwindows have
rank r+1 after the splice. Thus a missing old owner cannot reappear at a
different interval length. The untouched cycles carry none of the lost
owners, since the original owner palette was globally unique.

The native35 graft is not contradicted: its ports do not share this fixed
H-1 literal context/union, and its letters need not be the uniform maximal
erosion letters. The present result applies also to the common aperture
H=3 bank proposed by root, until its port letters or contexts are changed.

## 4. Full recency preservation cannot mix native apertures in a cycle

At every native aperture-H endpoint, Section 1 shows exactly H recency
prefix targets below rank s=r+1, so `b_s=H`. A legal recency update has
`Delta b_s<=1`; if equality holds its rank-s target is the same target
already present in the immediately previous state. This is the proved
rank-budget lemma in
`RECENCY_RANK_BUDGET_AND_SIXWAY_PORT_COST_INDEPENDENT_AUDIT_20260908.md`.

Distinct canonical state occurrences have distinct rank-s owners.
Therefore a legal edge between retained occurrences cannot increase H.
Any closed routing preserving the entire original state inventory must
stay at one aperture throughout each cycle. A linear routing can only
move through its retained aperture classes in decreasing order.

More generally, any ordinary word from the empty state that realizes
one of the original height-r recency states has `max b_s>=r`. The exact
identity `N-D_s=L+b_s(final)+E`, with total downward variation L, gives
`N-D_s>=max b_s>=r`. If it is universal, then `N>=W_r+r`; at17 this is
24318, already above 24313. This last obstruction requires literal
preservation of that native state; capping or retiming can change it.

## 5. Status

These are exact finite obstructions for natural collar/context methods
on the newly proved height-adaptive source. They do not assert that all
same-aperture sparse recency grafts fail. A successful next connector
must alter the common-context hypothesis, change the local envelopes,
or transport the affected middle targets through an explicitly different
literal mechanism. No generic unverified seam has been counted as free.
