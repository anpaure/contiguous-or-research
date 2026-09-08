#define main audit_hook_repair_unused_main
#include "audit_hook_repair.cpp"
#undef main

int main() {
    for (int m=1;m<=40;++m) {
        auto L=raw(true,m), R=rechainedRdiag(m);
        auto [pl,pr]=prec(L,R,m);
        std::cout<<m<<" L="<<L.size()<<" R="<<R.size()
                 <<" PL="<<topo(pl)<<" PR="<<topo(pr)<<"\n";
        if (m<=5) {
            auto a=onecycle(pl),b=onecycle(pr);
            std::cout<<" PLcycle";for(int x:a)std::cout<<" "<<L[x].s;
            std::cout<<"\n PRcycle";for(int x:b)std::cout<<" "<<R[x].s;
            std::cout<<"\n";
        }
    }
}
