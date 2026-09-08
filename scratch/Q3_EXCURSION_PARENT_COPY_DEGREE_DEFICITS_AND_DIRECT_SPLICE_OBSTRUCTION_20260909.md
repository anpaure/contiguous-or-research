# Exact deficits and an obstruction to directly splicing the q3 excursion bank

Date: 2026-09-09. Status: pure-proof audit; no execution or search.

The disjoint five-step excursion bank cannot be made into one cycle by
repairing its displaced edges solely inside an otherwise unchanged
parent10 copy. There is a dichotomy: either a free upper has no compatible
missing parent head, or some excursion components are already closed.
This does not rule out using further sectors together with suitable
additional changes. The exact residual matching graph is given below.

## 1. Notation and the precise height information

Use the hypotheses and Hall choices from the
[five-step bank audit](Q3_FIRST11_COLLISION_REPAIR_BY_SMALL_SHADOW_HALL_INDEPENDENT_AUDIT_20260909.md).
The old dimension is 2r+1, r>=7; the two new bits are a,b. Let sigma be
the parent lower-state Hamilton successor, Phi its canonical outgoing
matching, and u its first old coordinate. Put

    I = {root ports L},                 c=|I|=Cat_r,
    U_L=Phi(L)=L+u,
    P_L=sigma(L)=U_L-d_L,
    K_L=P_L-e_L,
    K'_L=J(K_L)-u,
    T_L=J(K'_L).

The distinct Hall-selected K_L contain u. Each excursion is

    L+a -> U_L -> P_L+b -> K_L+a+b -> K'_L+a+b -> T_L+a.       (1)

Write P=sigma(I), T={T_L:L in I}, and H=sigma^{-1}(T). The specified
excursion gives a bijection from I to T. All references to unchanged
parent edges below mean the lifted edges S+a -> sigma(S)+a through
Phi(S)+a, with the canonical outgoing matching held fixed.

Let m(S) be the minimum of the old +/-1 prefix walk, including the empty
prefix. The root walks L have m(L)=-1 and U_L has every nonempty prefix
at least 1. Deleting d_L reduces a suffix by two, so m(P_L)=-1, since
its total height is -1. Deleting e_L similarly gives m(K_L)=-3.
The first-minimum raising map raises the minimum by exactly one. Since
u is first and remains present in J(K_L), deleting u lowers every
nonempty prefix by two. Consequently

    m(J(K_L))=-2,    m(K'_L)=-4,    m(T_L)=-3.              (2)

Every T_L omits u, as proved by J injectivity in the bank audit.
Every P_L contains u. In particular I, P, T are pairwise disjoint.

For H_0 in H, put T_0=sigma(H_0). Since T_0 is a facet of Phi(H_0),
its prefix heights differ from those of Phi(H_0) by either zero or -2.
Using m(T_0)=-3 and m(Phi(H_0))=m(H_0)+1 gives

    m(Phi(H_0)) in {-3,-2,-1},
    m(H_0) in {-4,-3,-2}.                                (3)

Thus H is disjoint from both I and P. An overlap H intersect T is
possible and is allowed in every statement below.

## 2. Mandatory cuts and the exact degree deficit

Keep all old parent10 vertices and install all excursions (1). The old
edge L->P_L must be removed at each L in I, because the excursion now
uses its outgoing upper Phi(L)+a. The old edge H_0->sigma(H_0) must
also be removed at every H_0 in H, because that target in T now receives
the last edge of an excursion. The two cut-tail sets are disjoint, so
these are exactly 2c distinct required parent-edge cuts.

After precisely these cuts and the five-step additions, the remaining
degree deficits are EXACTLY:

* every H_0+a has its outgoing upper Phi(H_0)+a free;
* every P_L+a has no incoming upper;
* all other used lower vertices and uppers have their required degrees.

The I outgoing deficits are filled by the excursions; the T incoming
deficits are filled by their last edges. Each excursion contributes four
new lower vertices, all outside the parent10 sector. Its four additional
uppers are also outside the parent10 upper sector. The first upper is
the original Phi(L)+a, reused rather than counted twice. Therefore

    used lowers = used uppers = W_old+4c,
    assigned incoming edges = W_old+3c.                  (4)

This leaves c outgoing and c incoming sockets. The directed lower graph
is a disjoint union of exactly c open paths from P to H, together with
possibly some already-closed cycles. This description follows just from
the degree counts; it makes no Hamilton or residence conclusion.

## 3. Direct completion has a forced obstruction

Suppose only direct parent10 connections H_0+a -> P_L+a are allowed
to fill the remaining sockets, with no further parent or bank edge cut.
The exact incidence condition for such a connection is

    P_L subset Phi(H_0).                                 (5)

If H_0 omits u, then Phi(H_0) also omits u: otherwise H_0 would be a
root port in I, contrary to (3). But every P_L contains u. Hence this
mouth has no possible head in (5). Direct degree completion is impossible.

If H_0 contains u, the parent edge H_0->T_0 removes u, and necessarily

    Phi(H_0)=T_0+u.

Then (5) is equivalent to P_L-u subset T_0. Thus, even ignoring
connectivity, the direct completion problem is the specific balanced
containment matching from output r-sets T_0 to input (r-1)-sets P_L-u,
provided ALL mouths contain u. This Hall condition is not supplied by
the earlier Hall choice of the K_L.

However, when all H contain u, connectivity already fails independently
of that matching. Each H is a parent u-deletion tail. There are exactly
c such tails, because there are c u-insertions, namely the root ports I.
Thus H is the ENTIRE set of parent u-deletion tails. The two cut sets
alternate around the parent cycle as

    root insertion tail I, deletion tail H, I, H, ... .

Every untouched u=0 parent arc begins at some T=sigma(H) and ends at
the next root port I. The excursion bijection I->T followed by these
arcs induces a permutation of the c root ports. Its permutation cycles
are already-closed directed components. They include all excursions and
all parent u=0 states. The remaining parent u=1 arcs run from P to H.
Filling their sockets cannot join the already-closed components.

Therefore, for EVERY Hall choice in (1), one of the following holds:

    some mouth omits u, and direct degree completion is impossible;
    all mouths contain u, and the fixed graph already has a closed cycle.

In particular no direct parent10 completion can produce a single cycle
on all used vertices. In the second case, adding unused-sector paths
ONLY at the remaining H/P sockets still cannot help: at least one
additional already-fixed edge must be broken to join a closed component.
In the first case, unused-sector routing remains a possible escape.

This is a no-go for this precise direct-splice architecture. It is not
an impossibility theorem for the child dimension or for other grafts.

## 4. Exact component test before any further completion

There is a finite combinatorial description of every already-closed
component, using no new word search. Order the 2c cut tails I union H
around the original parent cycle and let tau be their cyclic successor.
For each L in I, let h(L)=sigma^{-1}(T_L) in H. The graft from L then
follows the untouched parent arc starting at T_L until it reaches

    tau(h(L)).                                           (6)

Iterating (6) as long as its output is again in I gives either a cycle
entirely in I or an open chain ending at H. The cycles correspond
exactly to the already-closed components. No completion using only free
sockets can merge any such component.

If there are no such cycles, contract each of the c open paths to one
vertex. Any further direct matching produces a permutation of these
contracted paths; it gives one cycle if and only if that permutation is
one cycle. Ordinary matching feasibility alone does not impose this.

No cut-order inventory or component computation was performed here.

## 5. The exact remaining-sector matching graph

Let V be all used child lower vertices from (4), and let Psi denote
canonical child Phi. The outgoing upper set is exactly Psi(V). Put

    Lambda = {all child middle lower states} minus V.

The remaining incoming matching graph has left and right classes

    left:  Psi(Lambda) union {Phi(H_0)+a : H_0 in H},
    right: Lambda union {P_L+a : L in I}.                 (7)

An edge means lower subset upper; exclude assigning an upper back to
its own outgoing lower if a strict directed cycle cover is required.
Both classes have exactly

    |Lambda|+c = W_child-W_old-3c                         (8)

vertices. A perfect matching in (7) is equivalent to filling all
remaining incoming degrees, giving a cycle cover with the fixed outgoing
matching. One-cycle connectivity, residence-three constraints at new
joins, and full interval-target coverage remain separate requirements.
An already-closed component from Section4 is an immediate obstruction
to a spanning completion that leaves all fixed edges intact.

There is a concrete available first step out of every mouth: the free
upper Phi(H_0)+a can enter the distinct 00-state Phi(H_0), deleting a.
This state is unused, since the existing 00 bank is Phi(I) and H is
disjoint from I. Deletion is residence-legal whenever the incoming
a-age is at least three; a global gluing proof must retain that condition.
These new 00 states do NOT have the positive old walks of the original
root00 bank. By (3) they have minimum at most -1, so the next canonical
child Phi adds an OLD coordinate, rather than immediately adding b.
Their subsequent routing is therefore a different sector problem.

The exact degree ledger, the direct-splice obstruction, and graph (7)
are proved without constructing a matching or altering any literal word.
