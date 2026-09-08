# Full-profile upper period and exact period for primitive rows

Date: 2026-09-08. Independent pure-proof audit by exact_b_finite_frontier.
No mathematical computation or word search was run.

Verdict: the proposed upper-period statement passes, including the
selection-count identity, the unchanged time parameter under reduction,
and the one-site terminal case.

Let n=2r+1, let f be the canonical physical PBBS map, and let

    n_s=2a_s+1,  n_0=n,  n_h=1

be the full original pruning profile, stopped at its one-site bottom.
Define

    M=lcm_{0<=s<h}(n_s n_(s+1)),

with the empty lcm equal to one when h=0. Then

    f^M(A)=A                                               (1)

for every state A with this profile, with no primitivity hypothesis.
Every physical minimal f-period is odd; the minimal f^2-period is the
same number. If every nonterminal incoming-gap row is primitive, these
two minimal periods are exactly M.

## 1. Exact physical conventions and retained reduction theorem

Sites and edges are labelled and fixed. Index the outgoing edge i as
the edge from site i to site i+1. A canonical f-update selects the
unique unmatched zero kappa and complements all other bits.

The exact one-step reduction is Theorem 14.1 and equation (14.4) of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`. Equality particles retain
their cyclic labels. Their recorded-bit word evolves by exactly ONE
canonical child f-update per parent update. If that child update selects
particle-label j, precisely parent particle j advances one physical edge.
All other parent particles stay put. There is no time division by either
the parent circumference or the particle count, and particle labels are
not reset when the current root changes.

The original row coordinates and the previously proved primitive-row lower
divisibility are recorded in
`PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`.
The argument below adds a return construction in the opposite direction.

## 2. Every return of a child system has uniform site-selection counts

Consider a labelled child system of odd size p>=3. Let b_i(t) be its bit
at site i and

    E_i(t)=1{b_i(t)=b_(i+1)(t)}.

At the selected unmatched zero kappa, the local bits are 0,0,1 on sites
kappa-1,kappa,kappa+1. This follows by rotating to its normalized Dyck
root: a nonempty Dyck tail starts with one and ends with zero.

After the update, edge kappa-1 changes from equal to unequal and edge
kappa changes from unequal to equal. Every other edge retains equality
status because both its endpoints are complemented. Thus, if C_i(T)
counts selections of site i during the first T updates,

    E_i(T)-E_i(0)=C_i(T)-C_(i+1)(T).                       (2)

If the full labelled child word returns at time T, all its edge indicators
return. Equation (2) makes all C_i(T) equal. Exactly one site is selected
in each update, so their sum is T and

    C_i(T)=T/p  for every i.                               (3)

In particular p divides T. This statement concerns an arbitrary genuine
return time, not necessarily the child's minimal period.

For p=1 the unique word is the single zero and f fixes it. Its sole site
is selected at every update, giving C_0(T)=T=T/p directly. The 0,0,1
argument is not applied to this degenerate case, whose two incident
edges coincide.

## 3. Lifting a common return through one physical level

Consider a parent of circumference n with p persistently labelled equality
particles. Its child word has p fixed labelled sites. Suppose the child
returns at time T and np divides T.

By the exact skew update, parent particle i advances one physical edge
each time child site i is selected. Choose integer lifts of particle
positions x_i. Equation (3), including the p=1 case, gives

    x_i(T)=x_i(0)+T/p.

Because np|T, the increment T/p is an integer multiple of n. Every
parent particle therefore returns to its own initial physical edge modulo
n, with its persistent label unchanged. The child return also restores
every particle's recorded bit on that same label.

The equality-edge set together with its recorded bits determines the
entire parent word. There is at least one equality edge; its recorded
bit fixes its endpoints, and one propagates around the circle, retaining
the bit on an equality edge and changing it on an unequal edge. Therefore
the restored positions and recorded bits imply that the parent word
itself returns at time T.

This proves the precise lifting lemma:

    child returns at T AND np|T  =>  parent returns at T.   (4)

No primitive-row condition, resampling, or hypothetical synchronization
of separate clocks is used. The same T counts parent and child updates.

## 4. Induct upward from the one-site bottom

For each level define

    M_s=lcm_{s<=j<h}(n_j n_(j+1)),  M_h=1.

At the bottom the one-site state is fixed, so every time is a return.
Assume the level s+1 child returns after M_(s+1) updates. It also returns
at every multiple of that number, since the dynamics is a permutation.
The integer M_s is a multiple of M_(s+1) and of n_s n_(s+1).
Applying (4) makes M_s a parent return time.

Induction proves f^(M_s) fixes the level-s state, and at s=0 proves (1).
Every n_j is odd, so every M_s is odd. A minimal period d_s divides its
return time M_s and is therefore odd. Squaring a permutation on an orbit
of odd length preserves its length. Thus the minimal f and f^2 periods
coincide at every level, even when some incoming-gap rows are nonprimitive.

## 5. Primitive rows make the upper bound exact

Let d be the minimal physical f-period of the original state, and assume
every one of its h nonterminal original rows is primitive. The synchronous
descent proved in the invariant-row lower-period audit applies at the
same return time d through every level. At level s it gives

    n_s n_(s+1) divides d.

Hence M|d. Section 4 gives d|M. Therefore d=M. Since d is odd, the
minimal original owner-cycle period under g=f^2 is also M.

When primitivity fails, the argument proves only d|M; equality need not
follow. All statements concern labelled physical returns, not returns
modulo rotation. No claim about exact optimal OR-word length follows from
this period theorem alone.
